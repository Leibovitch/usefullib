import cv2
import numpy as np


def median_masked_pooling(I, RF, stride, mask, resize=True):
    im_size = np.array(I.shape)
    steps = np.floor(im_size / stride).astype(int)
    pooled_median = np.zeros(steps)
    for i in range(steps[0]):
        for j in range(steps[1]):
            bottomi = i * stride
            upperi = np.min([i * stride + RF, im_size[0]])
            bottomj = j * stride
            upperj = np.min([j * stride + RF, im_size[1]])
            crop = I[bottomi:upperi, bottomj:upperj]
            edge_crop = mask[bottomi:upperi, bottomj:upperj]
            masked_crop = np.ma.array(crop, mask=np.logical_not(edge_crop))
            pooled_median[i,j] = np.ma.median(masked_crop)

    if resize:
        pooled_median = cv2.resize(pooled_median, I.shape, interpolation = cv2.INTER_NEAREST)
            
    return pooled_median