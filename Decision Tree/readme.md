# Decision Tree

Decision tree is decision based tool, structured in a tree architecture. Here every node represents a decision to be taken on the dataset and paves a path to its children based on the result of the decision. Decision tree can be used for both Classification and Regression problems in Supervised Learning.

Example, for categorising patients with high Blood Pressure, we might use these decisions:-
![High BP Decision Tree](https://github.com/Snorlexing/Machine-Learning-Basics/blob/master/Decision%20Tree/HIGH%20BP%20DECISION%20TREE.png)

The combination of decisions in a decision tree affects the accuracy of the results. So, it is important that decision rules are properly arranged to increase the efficiency of the decision tree.

To train a decision tree for better accuracy of results, we train our decision tree model using ID3(Iterative Dichotomiser 3) algorithm. In ID3 algorithm, the criteria for selecting a particular decision rule depends upon the change in information gain. For our problem of increasing the efficiency and accuracy of the decision tree, we prefer to use that decision rule which has the largest information gain.

Firstly we calculate the entropy associated with every decision, using the formula: -

![entropy](https://latex.codecogs.com/gif.latex?H(S)=\sum_{x\in&space;X}{-p(x)\log_2p(x)})

Here,
  * S – Represents the current dataset.
  * X – Represents the set of Classes in set S.
  * p(x) – Represents the proportion of elements x in the set S.

H(S) = 0, represents that the data points in the dataset S, belong to same class.
  
Now, using the entropy calculated above, we determine the information gain using the formula: - 
### ![infogain](https://latex.codecogs.com/gif.latex?IG(S,A)=H(S)-\sum_{t\in&space;T}p(t)H(t))

Here,
  * H(S) – Represents the entropy of set S.
  * T - Represents the subsets created using the attribute, A for dividing the set, S.
  * H(t) - Represents the entropy of the subset t.

ID3 algorithm is iteratively repeated for every node till the data belongs to same class or there is no attribute left for expansion.

## Advantages of ID3:
  1. It is a white-box model for transforming the input data to a desired output, i.e. the flow of the data can be analysed for a             particular decision leading to the predicted output.
  2. It is highly specific to a problem.
  3. It can handle both the numerical and categorical data types.
  4. It is easy to use and similar to human logical reasoning for taking decisions.
  5. It is robust to outliers, and missing values.

## Disadvatages of ID3:
  1. It does not guarentee an optimal solution i.e. it can converge to local optima.
  2. It can overfit the dataset.
  3. It can be harder to use for continuous data.

> Source: 
> * https://en.wikipedia.org/wiki/Decision_tree
> * https://en.wikipedia.org/wiki/ID3_algorithm
