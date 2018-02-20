import cv2
import numpy as np

#Transformada de exponencial

gama = 50
c = 1
def nothing(x):
    pass

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("img2", cv2.WINDOW_KEEPRATIO)
cv2.createTrackbar("Gama", "img2", gama, 1000, nothing)
cv2.createTrackbar("C", "img2", c, 255, nothing)

while(True):
    img = cv2.imread('./spectrum.tif', cv2.IMREAD_GRAYSCALE)
    img2 = np.zeros(img.shape, dtype=np.float64)

    gama = cv2.getTrackbarPos("Gama", "img2")
    c = cv2.getTrackbarPos("C", "img2")

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            intensity = img[x, y]
            intensity_new = np.power(intensity, gama/1000.0)
            img2[x, y] = intensity_new

    cv2.normalize(img2, img2, 1, 0, cv2.NORM_MINMAX)

    cv2.imshow('img', img)
    cv2.imshow('img2', img2)

    if cv2.waitKey(1) == ord('q'):
        break
