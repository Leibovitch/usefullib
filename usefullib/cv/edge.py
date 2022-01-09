import cv2
import numpy as np
from scipy.signal import convolve2d


def edge_width(edge_image, max_expected_edge, stride, RF):
    EWH = convolve2d(edge_image, np.ones((1, max_expected_edge)), mode='same')
    EWV = convolve2d(edge_image, np.ones((max_expected_edge, 1)), mode='same')
    EWD = convolve2d(edge_image, np.identity(max_expected_edge), mode='same')
    EWAD = convolve2d(edge_image, np.fliplr(np.identity(max_expected_edge)), mode='same')

    R = np.min(np.stack([EWH, EWV, EWD, EWAD]), axis=0)
    EW =  median_masked_pooling(R, RF, stride, RF)
    return EW


def median_masked_pooling(I, RF, stride, mask, resize=True):
    im_size = np.array(I.shape)
    steps = np.floor(im_size / stride).astype(np.uint8)
    pooled_median = np.zeros(steps)
    for i in range(steps[0]):
        for j in range(steps[1]):
            bottomi = i * stride
            upperi = np.min([i * stride + RF[0], im_size[0]])
            bottomj = j * stride
            upperj = np.min([j * stride + RF[1], im_size[1]])
            crop = I[bottomi:upperi, bottomj:upperj]
            edge_crop = mask[bottomi:upperi, bottomj:upperj]
            masked_crop = np.ma.array(crop, mask=np.logical_not(edge_crop))
            pooled_median[i,j] = np.ma.median(masked_crop)

    if resize:
        pooled_median = cv2.resize(pooled_median, I.shape, interpolation = cv2.INTER_NEAREST)
            
    return pooled_median

