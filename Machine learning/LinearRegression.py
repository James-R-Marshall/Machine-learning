# Linear regression is for continuous values, not discrete values.
# This can be used for predicting weight based on different features. 

# we use slope intercept form to create a function Y = WX+b
# W = weight (it is still the slope)

# To find W we use the MSE (Mean squared Error) W = MSE = 1/n*sum(from 1 to n){yi - (wx[i] + b)}^2 
# we use the derrivitive of the MSE to find the minimum value of the function. This is called the gradient.
# we need to find the minimum in respect to b and in respect to W
# look at notes for the mathematical formulas
# We use Greadient Decent to  find the minimum of the funciton, this is just taking steps down the function until we get to the
# bottom

# for each step we take, we update the weight and bias (W and B)
# W = W - a*DW  ,  and b = b-a*DB    **** a = learning rate   DW = derrivitive solved for w   , DB = derrivitive solved for B

# learning rate is important because it has to be just right, if it is too small it will make way too many steps 
# and that is bad for optimization. if it is too big it will go back and fourth on the funtion and spiral out of
# controll

import numpy as np

class LinearRegression:
    def __init__(self, lr = .001, n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
    def fit(self,X,y):
        # initialize parameters
        Shape = X.shape
        if len(Shape) == 2:
            n_samples = Shape[0]
            n_features = Shape[1]
        else:
            n_samples = Shape[0]
            n_features = 1
        self.weights = np.zeros(n_features)
        self.bias = 0

      
        # Gradient decent
        for _ in range (self.n_iters):
            if self.weights.size == 1:
                y_predicted = np.dot(X, self.weights[0]) + self.bias
            else:
                y_predicted = np.dot(X, self.weights) + self.bias
            dw = (1/n_samples) * np.dot(X.T, (y_predicted-y))
            db = (1/n_samples) * np.sum(y_predicted - y)
            self.weights -= self.lr*dw
            self.bias -= self.lr*db
    def predict(self,X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted
