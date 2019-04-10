# implement k-nearest neighbours classification algorithm
# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# calculate distance between two points
def dist(a, b):
    diff = a - b
    diff = diff * diff
    d = np.sqrt(sum(diff))
    return d


# determining the class of testing point
def classify(train, target, a, k):
    distance = []
    # calculating distance from all the points in the training dataset
    for i, t in enumerate(train):
        d = dist(t, a)
        distance.append((i, d))
    # sorting the distances maintaining the order
    distance = sorted(distance, key=lambda x: x[1])
    # separating k nearest neighbors
    knn = distance[:k]
    # maximum distance in k-nearest neighbors
    max_dist = knn[-1][1]
    neighbors = []
    for i in knn:
        neighbors.append(target.iloc[i[0]])
    # determining class
    u, c = np.unique(neighbors, return_counts=True)
    unique, count = zip(*sorted(zip(u, c), key=lambda x:x[1], reverse=True))
    return unique[0], max_dist


# read data from the input file
df = pd.read_csv("classify.csv")
# separating the features and target
features = np.array(df[["a", "b"]])
target = df[["t"]]
# testing data
a = np.array([1, 3])
b = np.array([2, 2])
c = np.array([4, 4])
# determination of the classes of these testing data
pred_a, radius_a = classify(features, target, a, 3)
print(a, "is associated with class ", pred_a)
pred_b, radius_b = classify(features, target, b, 7)
print(b, "is associated with class ", pred_b)
pred_c, radius_c = classify(features, target, c, 5)
print(c, "is associated with class ", pred_c)
# colors and markers for the plot
colors = ["r", "b"]
markers = ["^", "s"]
# plotting the data points
fig = plt.figure(figsize=(6, 6))
for i, k in enumerate(features):
    v = int(target.iloc[i])
    plt.scatter(k[0], k[1], c=colors[v], marker=markers[v])
plt.scatter(a[0], a[1], c="g")
plt.scatter(b[0], b[1], c="g")
plt.scatter(c[0], c[1], c="g")
# plotting the circles around the testing data points
circle1 = plt.Circle((a[0], a[1]), radius_a, fill=False)
plt.gca().add_artist(circle1)
circle2 = plt.Circle((b[0], b[1]), radius_b, fill=False)
plt.gca().add_artist(circle2)
circle3 = plt.Circle((c[0], c[1]), radius_c, fill=False)
plt.gca().add_artist(circle3)
plt.xlim((-0.5, 5.5))
plt.ylim((-0.5, 5.5))
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
