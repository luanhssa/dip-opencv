import cv2
import numpy as np


wsize = 1

img = cv2.imread('../../img/squares_noisy.tif', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("Original", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("New", cv2.WINDOW_KEEPRATIO)

cv2.imshow("Original", img)

while cv2.waitKey(1) != ord('q'):
    img2 = np.zeros(img.shape, dtype=np.float64)

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img2[y-wsize:y+wsize, x-wsize:x+wsize] = cv2.equalizeHist(img[y-wsize:y+wsize, x-wsize:x+wsize])

    # cv2.normalize(img2, img2, 1, 0, cv2.NORM_MINMAX)
    cv2.imshow("New", img2)
