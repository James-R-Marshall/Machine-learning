import LinearRegression as reg
import KNNAlgorythm as nn
import numpy as np

def main():
    #linear regression test
    lr = reg.LinearRegression()
    arr = np.array([[1,1],[2,3],[3,1],[4,2],[5,2],[6,1],[7,3]])
    Y   = np.array([1,4,3,5,8,7,10])
    lr.fit(arr,Y) 
    print(lr.predict([7,1]))

    # nearest neighbor algorithm test
    x=[[25,5],[30,6],[12,2],[4,2],[20,4],[25,15],[23,8],[15,10]]
    y=[2,2,1,1,1,2,3,3,3]

    nearest = nn.NearestNeighbor(k = 3)
    nearest.fit(x,y,2, 8)
    predictions = nearest.predict([5,2])
    print (predictions)

main()