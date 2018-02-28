# Log Transform
import cv2
import numpy as np


def nothing(x):
    pass


img = cv2.imread('../../img/spectrum.tif', cv2.IMREAD_GRAYSCALE)
img2 = np.zeros(img.shape, dtype=np.float64)


cv2.namedWindow("Spec", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("Spec New", cv2.WINDOW_KEEPRATIO)

c = 1

while True:
    intensity = img[:]
    img2[:] = c * np.log(1.0 + intensity)

    cv2.normalize(img2, img2, 1, 0, cv2.NORM_MINMAX)

    cv2.imshow('Spec', img)
    cv2.imshow('Spec New', img2)

    if cv2.waitKey(1) == ord('q'):
        break
