import cv2
import numpy as np

''' C++ code
Mat img = imreaad("tungsten.tif", IMREAD_GRAYSCALE);
MAT img2 = img.clone();
double E = 3.0,
        k0 = 0.4,
        k1 = 0.02,
        k2 = 0.4;
int wsize = 1;
Mat avg_global, avg_local, std_global, std_local;

meanStdDev(img, avg_global, std_global);
cout << avg_global.at<double>(0,0) << ", " << std_global.at<double>(0,0) << endl;
for (int y = wsize; y < img.rows - wsize; y++) {
    for (int x = wsize; x < img.cols; x++) {
        meanStdDev(img(Range(y-wsize, y+wsize), Range(x-wsize, x+wsize)), avg_local, std_local);
        if (
            (avg_local.at<double>(0,0) <= k0 * avg_global.at<double>(0,0)) &&
            (k1 * std_global.at<double>(0,0) <= std_local.at<double>(0,0)) &&
            (std_local.at<double>(0,0) <= k2 * std_global.at<double>(0,0))
            ) {
            img2.at<uchar>(y,x) = E * img.at<uchar>(y,x);
        }
    }
}
'''


def nothing(x):
    pass


img = cv2.imread('../../img/tungsten.tif', cv2.IMREAD_GRAYSCALE)
img2 = np.zeros(img.shape, dtype=np.float64)

E = 1
k0 = 0.4
k1 = 0.02
k2 = 0.4
wsize = 1
avg_global = 0
avg_local = 0
std_global = 0
std_local = 0

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("img2", cv2.WINDOW_KEEPRATIO)
cv2.createTrackbar("E", "img2", E, 10, nothing)

while True:
    (avg_local, std_global) = cv2.meanStdDev(img)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            (avg_global, std_local) = cv2.meanStdDev(img[x-wsize:x+wsize][y-wsize:y+wsize])
    intensity = img[:]
    img2[:] = (E*intensity) if (avg_local <= k0*avg_global and k1*std_global <= std_local and std_local <= k2*std_global) else intensity
    E = cv2.getTrackbarPos("E", "img2")

    cv2.normalize(img2, img2, 1, 0, cv2.NORM_MINMAX)

    cv2.imshow('img', img)
    cv2.imshow('img2', img2)

    if cv2.waitKey(1) == ord('q'):
        break
