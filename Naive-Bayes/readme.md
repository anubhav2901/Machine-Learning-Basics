# Naive Bayes Classifier
Naive bayes classifier is simple probabalistic classifier based on Bayes Theorem. This model applies Bayes theorem with an assumption of strong independence amongst the features. It was introduced in early 1960s for text categorization.

#### Bayes Theorem: - 
<a href="https://www.codecogs.com/eqnedit.php?latex=P(C_{k}|x)&space;=&space;\frac{P(x|C_{k})&space;*&space;P(C_{k})}{P(x)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(C_{k}|x)&space;=&space;\frac{P(x|C_{k})&space;*&space;P(C_{k})}{P(x)}" title="P(C_{k}|x) = \frac{P(x|C_{k}) * P(C_{k})}{P(x)}" /></a>

For naive bayes classifier we consider the features to be indepedent. Since evidence is same for every class therefore, the model will be concerned for the product of likelihood and prior.
Therefore, the Naive Bayes classifier model is:-
<a href="https://www.codecogs.com/eqnedit.php?latex=P(C_{k}|x)&space;=&space;P(C_{k})\prod_{i=1}^{n}P(x_{i}|C_{k})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(C_{k}|x)&space;=&space;P(C_{k})\prod_{i=1}^{n}P(x_{i}|C_{k})" title="P(C_{k}|x) = P(C_{k})\prod_{i=1}^{n}P(x_{i}|C_{k})" /></a>

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
