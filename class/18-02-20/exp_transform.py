import cv2
import numpy as np

#Transformada de exponencial

gama = 1
def nothing(x):
    pass

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("img2", cv2.WINDOW_KEEPRATIO)
cv2.createTrackbar("Gama", "img2", gama, 100, nothing)

while(True):
    img = cv2.imread('./spectrum.tif', cv2.IMREAD_GRAYSCALE)
    img2 = np.zeros(img.shape, dtype=np.float64)

    intensity = img[:]
    img2[:] = np.power(intensity, gama * 10 / 1000.0)

    gama = cv2.getTrackbarPos("Gama", "img2")

    cv2.normalize(img2, img2, 1, 0, cv2.NORM_MINMAX)

    cv2.imshow('img', img)
    cv2.imshow('img2', img2)

    if cv2.waitKey(1) == ord('q'):
        break
