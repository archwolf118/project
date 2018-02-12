# 基于内容的视频检索系统

**[测试网站]**：http://39.106.185.226/

**[功能描述]**：打开网页后，用户能够上传一个视频截图图片（jpg或者png），点击搜索之后，系统可以返回截图的来源视频，并且从此截图场景在视频中发生的时间点往前10秒开始播放来源视频。

**[开发环境]**：

- 视频下载："稞麦"下载器，视频截图用 vs2015\__c++__openCV 
- 特征提取：windows10\_\__python3.5\_\_jupyter notebook\_\_tensorflow\_\_keras
- 特征比对：nmslib
- 建站：flask
- 服务器：阿里云

**[视频来源]**：

•   <http://v.youku.com/v_show/id_XMzM4MTYwMDMxMg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2>

•   <http://v.youku.com/v_show/id_XMzM4MTMzMDAyNA==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2>

•   <http://v.youku.com/v_show/id_XMzM4MTQ0NTQ5Ng==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2>

•   <http://v.youku.com/v_show/id_XMzM4MDY0ODEyNA==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2>

•   <http://v.youku.com/v_show/id_XMzM4MTQ1NDI1Mg==.html?spm=a2h0k.8191407.0.0&from=s1.8-1-1.2>

**[网页结构]**：

```
├── README.md                   // 说明
├── webserver.py  	            // flask应用文件
├── static                      // 静态文件夹
│   ├── image                   // 上传图片位置
│   └── video                   // 视频存放位置
|       └── 1/2/3/4/5.mp4
├── template                    // 模板文件夹
│   └── index.html              // 网页文件
├── help.py                     // 帮助文件
├── vgg16_weights.h5            // vgg16模型参数（527M）****未上传****下载地址：                
├── labels.txt                  // 数据集的特征向量对应的标签（含有视频信息）       
└── new.csv                     // 数据集的特征向量
另附：
├── test_samples                //测试样本
├── videoSearching_v3.ipynb     //图片特征提取文件
└──  sample_extraction           //图片截取

注：vgg16模型参数未上传，下载地址：https://github.com/fchollet/deep-learning-models/releases
请将“vgg16_weights_tf_dim_ordering_tf_kernels.h5” 改名为vgg16_weights.h5
```

**[实现步骤]**：

1. 下载视频，每3秒（每隔45帧）截取一张图片加入数据集，每张图片的文件名包含**”视频信息“**，如1_495.jpg为编号为1的视频的第495帧。

2. 加载vgg16模型（去掉最后两层），输出图片数据集对应的特征集，存入csv文件，同时保存**索引文件**labels.txt。

3. 按上述方法对"测试样本"进行特征提取，然后用nmslib查询库输出“特征集”中最匹配的index，然后从索引文件labels.txt 中提取对应”图片名“，也即**”视频信息“**。

4. 播放

   注：网页具体实现见webserver.py 和 template/index.html

**[作者]**：陈鸣

**[联系方式]**：9304346@qq.com