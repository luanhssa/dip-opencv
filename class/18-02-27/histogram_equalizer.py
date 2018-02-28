# Histogram Equalizer
import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):
    pass


img = cv2.imread('./pollen_washedout.tif', cv2.IMREAD_GRAYSCALE)
img2 = np.zeros(img.shape, dtype=np.float64)

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("img2", cv2.WINDOW_KEEPRATIO)

while True:
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    img2 = cdf[img]

    # img2 = cv2.equalizeHist(img)

    cv2.imshow('img', img)
    cv2.imshow('img2', img2)
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()

    if cv2.waitKey(1) == ord('q'):
        break
