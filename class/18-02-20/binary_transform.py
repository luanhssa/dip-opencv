import cv2
import numpy as np

#Limearizacao por partes (binaria)

minor = 50
major = 1
def nothing(x):
    pass

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("img2", cv2.WINDOW_KEEPRATIO)
cv2.createTrackbar("Minor", "img2", minor, 255, nothing)
cv2.createTrackbar("Major", "img2", major, 255, nothing)

while(True):
    img = cv2.imread('./kidney.tif', cv2.IMREAD_GRAYSCALE)
    img2 = np.zeros(img.shape, dtype=np.float64)

    minor = cv2.getTrackbarPos("Minor", "img2")
    major = cv2.getTrackbarPos("Major", "img2")

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            intensity = img[x, y]
            intensity_new = ((intensity >= minor) and (intensity <= major)) if 1 else 0
            img2[x, y] = intensity_new

    cv2.normalize(img2, img2, 1, 0, cv2.NORM_MINMAX)

    cv2.imshow('img', img)
    cv2.imshow('img2', img2)

    if cv2.waitKey(1) == ord('q'):
        break
