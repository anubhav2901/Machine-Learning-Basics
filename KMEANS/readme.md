# K-MEANS CLUSTERING ALGORITHM
K-Means is an unsupervised learning algorithm, used for determining the clusters of data points having similar properties.
In this algorithm, centroids of k clusters are at first randomly initialised then, data points are assigned a cluster depending on the proximity of the centroid of a particular cluster. Then, the hypothesized centroids are updated to the centroids of the clusters formed. This is procedure followed until there is no significant change in the position of the centroids.

![Kmeans](https://github.com/Snorlexing/Machine-Learning-Basics/blob/k-mean-edit/KMEANS/kmeans.png)
#### Fig. (Trainsition of predicted mean values towards actual means of clusters.)

K-means is NP-hard problem, i.e. it is not computationally feasible to determine how many iterations the algorithm will run before halting. However, using efficient Heuristic algorithms the algorithm can converge to a local optima quickly.

### Advantages of K-means:-
  1. It can quickly converge to local optima.
  2. Lesser number of hyperparameters to tune i.e. only number of the clusters (K) is to be determined.

### Disadvantages of K-means:-
  1. Convergence to local optima quickly, reduces the chances of optimising the clusters and might produce incorrect results.
  2. Inappropriate choice of K can results in faulty clusters.

> Source: https://en.wikipedia.org/wiki/K-means_clustering
