import numpy as np
import random
# Choose k points randomly
d = 5 # dimension
m = 100
k = 10
x = np.random.rand(m, d)


def k_means(X, k, max_iteration):
    m, d = X.shape
    k_means = np.random.rand(k, d)
    for i in range(max_iteration):
        new_k = recompute_means(X, assignments(X, k_means))
        if (k_means == new_k).all():
            break
        k_means = new_k
    return k_means

def assignments(X, means):
    m, d = X.shape
    k = means.shape[0]
    assignment_dict = dict(zip(range(k), [[] for i in range(k)])) #ith index in this list is an integer where the ith point of X is clustered into
    for i in range(m):
        assignment_idx = 0
        min = float('inf')
        for j in range(k):
            dist = np.linalg.norm(X[i, :] - means[j, :])
            if dist < min:
                min = dist
                assignment_idx = j
        assignment_dict[assignment_idx] += [i]

    return assignment_dict

def recompute_means(X, assignments):
    """

    :param X:
    :param assignments: a dictionary whose ith element is the list of points contained in ith cluster
    :return:
    """
    k = len(assignments)
    d = X.shape[1]
    new_means_arr = np.zeros((k, d))
    for i in range(k):
        new_mean = np.zeros(d)
        points_idx_list = assignments[i]
        for idx in points_idx_list:
            new_mean += X[idx, :]
        new_mean /= len(points_idx_list)
        new_means_arr[i, :] = new_mean

    return new_means_arr
print(k_means(x, k, 1000))




