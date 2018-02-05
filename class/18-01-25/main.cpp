#include <QApplication>
#include <opencv2/opencv.hpp>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    cv::Mat img = cv::imread("../dog.jpg", cv::IMREAD_COLOR);
    cv::namedWindow("dog", cv::WINDOW_KEEPRATIO);
    cv::imshow("dog", img);

    return a.exec();
}
