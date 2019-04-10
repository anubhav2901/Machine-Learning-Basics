# K-Nearest Neighbors
K-Nearest Neighbors is a non-parameteric learning algorithm method which can be used for both the classification and regression problems. 
This algorithm predicts a value for unknown data, on the basis of the characteristics of its k nearest neighbors. Hence, it is named K-Nearest Neighbors algorithm. For the problem of classification, a class is assigned to the test data depending on the proximity of the test data to the data points of that particular class. For the problem of Regression, a prediction value is generated based on the average value of the target values of the data points in its proximity.

![KNN](https://github.com/Snorlexing/Machine-Learning-Basics/blob/knn-edit/KNN/knn.png)

### Effect of different values of Hyperparameter K:-
  * K is generally assigned an odd value to avoid the case of equal number of data points belonging to both classes being selected as the   nearest neighbors of a test data point.
  * Large values of K reduces the effects of noise in the dataset. But, it has a drawback that the decision boundary between the classes      becomes less distinct.
    * A special case is that of K being equal to the number of data points in the input dataset. Here, the KNN algorithm will prefer the         majority class. If the distance factor is included for the voting, KNN tranforms to K-means classification algorithm where a class         is predicted on the basis of the proximity of the test data point to the centroid of the class.
  * If K = 1, the class will be predicted on the basis of the nearest data point. This time the algorithm becomes sensitive to noise and     its performance degrades.
  
### Advantages of KNN:-
  1. It is very simple in implementation.
  2. No explicit training is required, as the input data provides the only required structure for prediction. 
  3. It is robust to outliers in the training data.
  4. Lesser number of hyperparameters required for tuning i.e. only the value of K is to be estimated.

### Disadvatages of KNN:-
  1. It suffers from the problem of "Majority Voting", i.e. it is possible that the test data point is near to a particular class but the   number of such data points in the set of nearest neighbors is in minority. So, the data point is misclassified. This problem can be       accounted by including a weight value of distance while counting the votes for the class.
  2. It is also known as lazy-learning method. Since to determine the neighbors of the test data points, the algorithm iterates through     whole dataset which can be a hectic task for larger datasets.
  
> Source: https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
