# Class day 18-02-27 - Image Enhancement

## Histogram Equalizer

```
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]
```

Pollen Washedout | Histogram Equalizer
:----------------:|:------------------:
![Pollen Washedout](pollen_washedout.png) | ![Histogram Equalizer](pollen_washedout_hist-eq.png)

---

##  