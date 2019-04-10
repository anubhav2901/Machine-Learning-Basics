# k-means clustering
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

INF = 1e12


# calculate distance
def dist(a, b):
    d = a - b
    d = d * d
    norm_d = d.sum()
    return np.sqrt(norm_d)


# determine the nearest cluster
def cluster_index(mean, v):
    min_d = INF
    index = 0
    c = 0
    for i in mean.values():
        d = dist(i, v)
        if d < min_d:
            min_d = d
            index = c
        c += 1
    return index


# determine shift in mean
def diff(prev_mean, mean, k):
    c = 0
    for i in range(k):
        d = dist(prev_mean[i], mean[i])
        if d != 0:
            c = 1
            break
    return c


# k-mean cluster algorithm
def k_means(data_set, k, iterations):
    cluster = {}
    mean = {}
    prev_mean = {}
    # determining random k mean values
    rows = data_set.shape[0]
    index = random.choices(range(rows), k=k)
    l = 0
    for i in index:
        prev_mean[l] = np.zeros(data_set.shape[1])
        mean[l] = data_set.iloc[i, :]
        l += 1
    error = diff(prev_mean, mean, k)
    # to determine path of mean values
    path = {}
    for i in range(k):
        path[i] = []
    # determining new means
    j = 0
    while error == 1:
        prev_mean = mean.copy()
        # making k clusters
        for i in range(k):
            cluster[i] = []
        for i in data_set.values:
            c = cluster_index(mean, i)
            cluster[c].append(i)
        for i in range(k):
            mean[i] = np.mean(cluster[i], axis=0)
            path[i].append(mean[i])
        error = diff(prev_mean, mean, k)
        j += 10
        if j % 1000 == 0:
            print("1")
    return cluster, path


# read data file
df = pd.read_csv("k_means_data.csv")
# number of clusters
k = 3
cluster, path = k_means(df, k, 10000)
# plotting the clusters
fig = plt.figure()
color = ["r", "b", "g", "y"]
for i in range(k):
    l_x, l_y = [], []
    for t in cluster[i]:
        l_x.append(t[0])
        l_y.append(t[1])
    plt.scatter(l_x, l_y, c=color[i])
    p_x, p_y = [], []
    for t in path[i]:
        p_x.append(t[0])
        p_y.append(t[1])
    plt.plot(p_x, p_y, c="#050505", marker="X")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.title("K - Means clustering")
plt.legend(["Mean 1", "Mean 2", "Mean 3", "Cluster 1", "Cluster 2", "Cluster 3"])
plt.show()
