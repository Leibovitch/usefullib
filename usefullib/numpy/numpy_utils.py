import random
import numpy as np

def sortby(array_list, sortby_index, ascending=True):
    combined_array = np.vstack(array_list).T
    sortedArr = combined_array[combined_array[:, sortby_index].argsort()]
    sorted_arrays = []
    for i in range(len(array_list)):
        sorted_arrays.append(sortedArr[:, i])

    if (ascending and sorted_arrays[sortby_index][-1] < sorted_arrays[sortby_index][0]) or (not ascending and sorted_arrays[sortby_index][-1] > sorted_arrays[sortby_index][0]):
        for i, arr in enumerate(sorted_arrays):
            sorted_arrays[i] = arr[::-1]

    return sorted_arrays

def rotate_2D_points(points, deg_angle):
    angle = np.deg2rad(deg_angle)
    dR = np.array([[np.cos(angle), np.sin(angle)],[-np.sin(angle), np.cos(angle)]])
    return dR @ points

def argmin_many(x):
    min_indecies = np.squeeze(np.argwhere(x == np.min(x)))
    return min_indecies

def argmax_many(x):
    min_indecies = np.squeeze(np.argwhere(x == np.min(x)))
    return min_indecies

def squeeze_to_array(a):
    # similar to numpy squeeze but retains at least one dimension
    dims = np.array(a.shape)
    if np.any(dims > 1):
        return np.squeeze(a)

    else:
        return np.array([np.squeeze(a)])

def sample_points(point_set, sample_number):
    number_of_points = point_set.shape[1]
    sample_indecies = random.sample(number_of_points, sample_number)
    return point_set[:, [item in sample_indecies for item in list(range(number_of_points))]]


# affine matrix calculous
def homogenize_set(X):
    return np.vstack([X, np.ones((1, X.shape[1]))])


def affine(T, X):
    return T @ homogenize_set(X)


def inverse_affine(T):
    t = np.expand_dims(T[:, 2], axis=1)
    A = T[:, 0:2]
    invA = np.linalg.inv(A)
    invT = np.hstack([invA, -invA @ t])
    return invT


def affine_normalize(X):
    set_mean = np.expand_dims(np.mean(X, axis=1), axis=1)
    set_std = np.expand_dims(np.std(X, axis=1), axis=1)
    NT = np.hstack([np.identity(len(set_mean)), np.zeros(set_mean.shape)])
    np.fill_diagonal(NT, 1 / set_std)
    NT[:, -1] = -(set_mean / set_std)[:, 0]
    return NT, affine(NT, X)


def compose_affine(T2, T1):
    # calculates T2 * T1
    A1 = T1[:, 0:2]
    A2 = T2[:, 0:2]
    t1 = np.expand_dims(T1[:, 2], axis=1)
    t2 = np.expand_dims(T2[:, 2], axis=1)
    combined_A = A2 @ A1
    combined_t = A2 @ t1 + t2
    return np.hstack([combined_A, combined_t])