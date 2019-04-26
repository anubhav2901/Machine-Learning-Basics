# naive bayes algorithm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# determining number of feature values
def naive_bayes(feature, target):
    # unique values of feature
    unique_values = np.unique(feature)
    # unique target values
    classes = np.unique(target)
    # sorting unique target values
    classes.sort()
    # map for storing count
    count = {}
    for i in unique_values:
        count[i] = np.zeros(2)
    # joining for iterating through both the vectors simultaneously
    ds = np.column_stack((feature, target))
    for t in ds:
        if t[1] == classes[0]:
            count[t[0]][0] += 1
        else:
            count[t[0]][1] += 1
    return count


# for predicting the class
def test(train, tup, target):
    # probability of each class
    probability = [0, 0]
    for i in range(2):
        p = 1
        c = 0
        for t in train.keys():
            p *= train[t][tup[c]][i] / target[i]
            c += 1
        probability[i] = p * target[i] / sum(target)
    # returning class having higher probability
    return probability.index(max(probability))


# read data file
df = pd.read_csv("pca_data.csv")
# separating features
features = df[["age", "year", "nodes"]]
# separating target variable
target = df[["survival"]] - 1
# counting total number of occurrences of classes
target_values = list(target["survival"].value_counts())
columns = list(features.columns)
# storing number classes associated with each feature class
train = {}
for i in columns:
    train[i] = naive_bayes(features[i], target)

# reading testing data file
ds = pd.read_csv("naive_bayes_test.csv")
test_features = ds[["age", "year", "nodes"]]
test_output = ds[["survival"]] - 1

# testing the model created
test_cases = ds.shape[0]
error = 0
for i in range(test_cases):
    predicted_class = test(train, test_features.iloc[i, :], target_values)
    if predicted_class != int(test_output.iloc[i, :]):
        error += 1

# printing error in prediction
print("ERROR IN PREDICTION : ", error / test_cases * 100, "%")

# plotting graph

