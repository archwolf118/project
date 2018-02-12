#include <opencv2\opencv.hpp>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include <stdio.h>
using namespace cv;

int main() {

	//读入视频
	//VideoCapture capture(0);
	VideoCapture capture("D:\\video\\5.mp4");
	char *SavePath = "D:\\截图\\";
	//循环显示
	int count_tmp = 0;
	char filename[100] = { '\0' };
	Mat frame;
	while (true) {
		capture >> frame;
		if (count_tmp % 45 == 0) {
			//定义一个Mat变量，用于存储每一帧的图像
			//读取当前帧
			//imshow("读取视频", frame);
			sprintf_s(filename, "%s//5_%d.jpg", SavePath, count_tmp);
			imwrite(filename, frame);
			//waitKey(3000);
		}
		++count_tmp;
		if (frame.empty()) break;
	}


	return 0;
}