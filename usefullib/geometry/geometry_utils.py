import numpy as np

def point_set_from_crop(crop):
    [Yt, Xt] = np.nonzero(crop)
    return np.vstack([Xt, Yt])

def set_ditances(X1, X2, norm):
    # X1 and X2 are point sets of size dims x N1, dims x N2
    dims = X1.shape[0]
    ds = np.zeros((X1.shape[1], X2.shape[1]))
    for alpha in range(dims):
        if norm < 100:
            ds += np.abs((np.expand_dims(X1[alpha, :], axis=1) - np.expand_dims(X2[alpha, :], axis=0))) ** norm

        else:
            durrent_diff = np.abs((np.expand_dims(X1[alpha, :], axis=1) - np.expand_dims(X2[alpha, :], axis=0)))
            ds = np.max(np.stack([ds, durrent_diff], axis=2), axis=2)
            print('max')
     
    if norm < 100:       
        return ds ** (1 / norm)

    else:
        return ds

def spherical_projection(point_set, R):
    xs = point_set[0, :]
    ys = point_set[1, :]
    scalars = xs ** 2 + ys ** 2 + R ** 2
    transformedX = 2 * xs * R / scalars
    transformedY = 2 * ys * R / scalars
    return np.stack([transformedX, transformedY], axis=0)

def lp_norm_transform():
    pass
