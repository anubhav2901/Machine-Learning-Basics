# create decision tree
import math
import pandas as pd


class DecisionTree:
    # assigning data set to every node
    def __init__(self, data_set):
        self.data_set = data_set
        self.visited_features = []
        self.feature = [i for i in data_set.keys()]
        self.target = self.feature[-1]
        self.feature = self.feature[:-1]
        self.child = {}
        self.entropy = self.data_entropy(data_set)
        self.split_feature = ""
        self.determined_class = ""

    # differentiate visited and non-visited features
    def visit(self):
        self.feature = list(filter(lambda x: x not in self.visited_features, self.feature))
        if self.entropy == 0:
            self.determined_class = str(self.data_set[self.target].unique()[0])

    # calculate average feature entropy
    def avg_feature_entropy(self, feature):
        feature_class = self.data_set[feature].unique()
        total_count = self.data_set.shape[0]
        feature_entropy = 0.0
        for i in feature_class:
            new_data = self.data_set[self.data_set[feature] == i]
            total = new_data.shape[0]
            feature_class_entropy = self.data_entropy(new_data)
            feature_entropy += (total / total_count) * feature_class_entropy
        return feature_entropy

    # calculate average data set entropy
    def data_entropy(self, data_set):
        values_count = data_set[self.target].value_counts()
        yes_value = 0 if "Yes" not in values_count else values_count["Yes"]
        no_value = 0 if "No" not in values_count else values_count["No"]
        total_count = data_set.shape[0]
        data_entropy = 0.0
        if yes_value != 0:
            frac_y = yes_value / total_count
            data_entropy += -frac_y * math.log2(frac_y)
        if no_value != 0:
            frac_n = no_value / total_count
            data_entropy += -frac_n * math.log2(frac_n)
        return data_entropy

    # calculate info gain of a feature
    def info_gain(self, feature):
        avg_feature_entropy = self.avg_feature_entropy(feature)
        return self.entropy - avg_feature_entropy

    # splitting according to maximum information gain
    def node_split(self):
        if len(self.feature) < 1 or self.entropy == 0:
            return {}
        max_info_gain = 0
        split_feature = self.feature[0]
        for i in self.feature:
            info_gain = self.info_gain(i)
            if info_gain > max_info_gain:
                split_feature = i
                max_info_gain = info_gain
        self.split_feature = split_feature
        attribute_list = self.data_set[split_feature].unique()
        child = {}
        for i in attribute_list:
            data = self.data_set[self.data_set[split_feature] == i]
            newnode = DecisionTree(data)
            newnode.visited_features = self.visited_features[:]
            newnode.visited_features.append(split_feature)
            newnode.visit()
            child[i] = newnode
        return child


def test_decision_tree(test, root):
    if root.determined_class != "":
        return root.determined_class
    else:
        split_feature = root.split_feature
        feature_class = root.data_set[split_feature].unique()
        for i in test:
            if i in feature_class:
                return test_decision_tree(test, root.child[i])
        return


# reading input file
df = pd.read_csv("train_data.csv", index_col="day")

# printing input file
features = list(df.keys())
target = features[-1]
features.remove(target)

# creating root node
root = DecisionTree(df)

# create a queue with root node for level order traversal
queue = [root]

# level order traversal
while len(queue) > 0:
    node = queue[0]
    queue.pop(0)
    if node.entropy == 0:
        continue
    node.child = node.node_split()
    for i in node.child.keys():
        queue.append(node.child[i])

# testing of decision tree created
# read test file
test = pd.read_csv("test_data.csv")
# read test output file
test_output = pd.read_csv("test_output.csv")

# set initial values
correct_output = 0
total_test = test.shape[0]
# to collect predicted values
predicted_output = []

# test the decision tree
for t in test.values:
    predicted_output.append(test_decision_tree(t, root))

# determine error in prediction
k = 0
for i in test_output.values:
    if i == predicted_output[k]:
        correct_output += 1
    k +=1

print("ERROR IN PREDICTION: ", correct_output / total_test * 100, "%")
