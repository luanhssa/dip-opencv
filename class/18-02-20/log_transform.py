import cv2
import numpy as np

#Transformada de logaritmica

img = cv2.imread('./spectrum.tif', cv2.IMREAD_GRAYSCALE)
img2 = np.zeros(img.shape, dtype=np.float64)

c = 1
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        intensity = img[x, y]
        intensity_new = c * np.log(1 + intensity)
        img2[x, y] = intensity_new

cv2.normalize(img2, img2, 1, 0, cv2.NORM_MINMAX)

cv2.namedWindow("Spec", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("Spec New", cv2.WINDOW_KEEPRATIO)
cv2.imshow('Spec', img)
cv2.imshow('Spec New', img2)

while(True):
    if cv2.waitKey(1) == ord('q'):
        break
