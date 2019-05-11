# Naive Bayes Classifier
Naive bayes classifier is simple probabalistic classifier based on Bayes Theorem. This model applies Bayes theorem with an assumption of strong independence amongst the features. It was introduced in early 1960s for text categorization.

#### Bayes Theorem: - 
![bayestheorem](https://latex.codecogs.com/gif.latex?p(C_k|X)=\frac{p(X|C_k)p(C_k)}{p(X)})

For naive bayes classifier we consider the features to be indepedent. Since evidence is same for every class therefore, the model will be concerned for the product of likelihood and prior.
Therefore, the Naive Bayes classifier model is:-
![naivebayes](https://latex.codecogs.com/gif.latex?p(C_k|X)=p(C_k)\prod_{i=1}^{n}p(x_i|C_k))

The class having the maximum value of the prosterior probability, that class will be assigned to the unknown data point (*x*).

#### Advantages of Naive Bayes Classifier: - 
* It is a very simple probability based classification model. 
* It can handle both discrete and continuous data.
* It requires no parameter for learning and it is robust to irrelevant features.
* It requires less number of training data.
* If there is conditional independence amongst the features, it will converge faster than other algorithms like Linear regression etc.

#### Disadvantages of Naive Bayes Classifier: -
* It cannot learn the interaction amongst the features.
* It is inefficient for very large and complex datasets.

>Source: https://en.wikipedia.org/wiki/Naive_Bayes_classifier
