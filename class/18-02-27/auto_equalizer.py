import cv2
import numpy as np

# automatic equalizer


def nothing(x):
    pass


img = cv2.imread('../../img/dollar.tif', cv2.IMREAD_GRAYSCALE)
img2 = np.zeros(img.shape, dtype=np.float64)

slice = 0

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("img2", cv2.WINDOW_KEEPRATIO)
cv2.createTrackbar("slice", "img2", slice, 7, nothing)

while True:
    intensity = img[:]
    img2[:] = intensity & (np.power(2, (7 - slice) + 1) - 1)
    slice = cv2.getTrackbarPos("slice", "img2")

    cv2.normalize(img2, img2, 1, 0, cv2.NORM_MINMAX)

    cv2.imshow('img', img)
    cv2.imshow('img2', img2)

    if cv2.waitKey(1) == ord('q'):
        break
