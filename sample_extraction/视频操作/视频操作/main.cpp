#include <opencv2\opencv.hpp>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include <stdio.h>
using namespace cv;

int main() {

	//������Ƶ
	//VideoCapture capture(0);
	VideoCapture capture("D:\\video\\5.mp4");
	char *SavePath = "D:\\��ͼ\\";
	//ѭ����ʾ
	int count_tmp = 0;
	char filename[100] = { '\0' };
	Mat frame;
	while (true) {
		capture >> frame;
		if (count_tmp % 45 == 0) {
			//����һ��Mat���������ڴ洢ÿһ֡��ͼ��
			//��ȡ��ǰ֡
			//imshow("��ȡ��Ƶ", frame);
			sprintf_s(filename, "%s//5_%d.jpg", SavePath, count_tmp);
			imwrite(filename, frame);
			//waitKey(3000);
		}
		++count_tmp;
		if (frame.empty()) break;
	}


	return 0;
}