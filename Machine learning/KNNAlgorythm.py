## this is the K Nearest Neighbors problem in python, you give this algorythm training examples 
## and then you give it a value where it will check where it is and what the closest nodes are
## based on which node has more close to the input you put in it will classify that new node as that type.
## define feature vectors

## in order to calculate distances use eucledian distance D = sqrt((x2-x1)^2 + (y2-y1)^2)
##this si the pythagorean therom 

#import numpy as np
#from collections import Counter
#def euclideanDistance(x1, x2):
#        return np.sqrt(np.sum((x1 - x2)**2))

#class NearestNeighbor:
#    def __init__(self, k=3):
#        self.k = k

#    def fit(self, X, y):
#        self.x_train = X
#        self.y_train = y
    
#    def predict(self,X):
#        predicted_labels = [self._predict(x) for x in X]
#        return np.array(predicted_labels)
        
#    def _predict(self,x):
#        #compute distances 
#        distances = [euclideanDistance(x, x_train) for x_train in self.x_train]
#        #get k nearest samples
#        k_indices = np.argsort(distances)[:self.k]
#        #get labels
#        k_nearest_labels = [self.y_train[i] for i in k_indices]
#        #maturity vote (most common class label)
#        most_common = Counter(k_nearest_labels).most_common(1)
#        return most_common[0][0]

#def main():
#    x = [1,1,1,3,3,4,2,3,5,6,7,8,7,6,5,7]
#    y = [0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1]

#    nearest = NearestNeighbor(k = 3)
#    nearest.fit(x,y)
#    predictions = nearest.predict([3,4,5])
#    print (predictions)


#main()







# this is a more universal algorythm that uses a 2d array to store a dynamic variable set so that we can change how many features we have. I created this one on my own.

import numpy as np
from collections import Counter
def euclideanDistance(xArr, xTrain, Features, Sets):
    sum = 0.0
    arr = [0]*Sets
    for i in range(Sets):
        for x in range(Features):
            sum += np.sqrt(np.sum((xArr[x] - xTrain[i][x])**2))
        arr[i] = sum
        sum = 0
    return arr

class NearestNeighbor:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X2DArray, yArray, numFeatures, numSet):
        self.x_train = X2DArray
        self.y_train = yArray
        self.Features = numFeatures
        self.Sets = numSet
    
    def predict(self,X):
        predicted_labels = self._predict(X)
        return np.array(predicted_labels)
        
    def _predict(self,X):
        #compute distances 

        Distance = euclideanDistance(X,self.x_train, self.Features, self.Sets) 
    #get k nearest samples
        k_indices = np.argsort(Distance)[:self.k]
    #get labels
        k_nearest_labels = [self.y_train[i] for i in k_indices]
    #maturity vote (most common class label)
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]


