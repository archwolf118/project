#encoding: utf-8

import os
import numpy as np
import nmslib as nl
from flask import Flask, request,render_template
from werkzeug.utils import secure_filename
from help import VGG_16,featureOuts

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'JPG'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.realpath(__file__))

# max document < 16M
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

data = np.loadtxt(os.path.join(app.config['UPLOAD_FOLDER'], 'new.csv'),delimiter=",")
f = open(os.path.join(app.config['UPLOAD_FOLDER'], 'labels.txt'),'r')
lines = f.readlines()
f.close()

index_1 = nl.init(method='hnsw', space='l2')
index_1.addDataPointBatch(data)
index_1.createIndex({'post': 2}, print_progress=True)

model = VGG_16(os.path.join(app.config['UPLOAD_FOLDER'], 'vgg16_weights.h5'))

html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>视频搜索</h1>
    <p>请上传图片(图片格式：jpg或png)</p>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=搜索>
    </form>
    '''

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],'static/image', filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'static/image',filename)

            sample = featureOuts(filepath, model)
            ids, distances = index_1.knnQuery(sample, k=4)
            vedio_index = lines[ids[0]][7]
            frame_index = int(lines[ids[0]][9:-5])

            time_index = 0
            if (frame_index//15 - 10) > 0:
                time_index = frame_index // 15 - 10

            return render_template("index.html",i = time_index,j=vedio_index)
    return html

if __name__ == '__main__':
    app.run()