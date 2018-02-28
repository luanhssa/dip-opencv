#include <QApplication>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;
using namespace std;

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    //*
    int thresh = 127;
    Mat img = imread("../dog.jpg", IMREAD_GRAYSCALE);
    Mat bin;
    namedWindow("bin", WINDOW_KEEPRATIO);

    createTrackbar("thresh", "bin", &thresh, 255, 0);

    img = img > 127 & img < 150;
    //imshow("dog", img);

    for(;;) {
        bin = img > thresh;
        imshow("bin", bin);
        if((char) waitKey(1) == 'q') break;
    }
    //  */

    /*
    Mat img = Mat::zeros(3, 3, CV_8U);
    cout << img << endl;
    // */

    /*
    Mat img = Mat::zeros(500, 500, CV_8UC1);
    cv::randu(img, 0, 255);
    imshow("img", img);
    waitKey(0);
    // */

    return 0;
}
