import enum
import numpy as np
class FindS:
    """This class is for taking a specific hyhpothesis and generalizing it until it matches all sucessful cases"""


    # in our arrays the values in order is as follows
    # {clean / dirty / normal, good smelling / not good smelling, talks / cant talk, pink / grey / brown / tan , fail / success} 
        
    index = 0
    exdata =([1, 3, 2, 1, 1],
                [1, 3, 1, 3, 0],
                [2, 3, 2, 1, 1],
                [2, 2, 2, 3, 1])
    hypothesis = None

    def fit(self, arr):

        self.num_elements = np.shape(arr)[1]
        self.num_samples = np.shape(arr)[0]
        self.hypothesis = arr[0];
        for row in arr:
            self.index = 0
            if(row[self.num_elements - 1] != 0):
                for cell in row:
                    if cell == self.hypothesis[self.index]:
                        pass
                    else:
                        self.hypothesis[self.index] = None
                    self.index+=1

    def ShowHypothesis(self):
        return self.hypothesis
    def printHypothesis(self):
        for item in self.hypothesis:
            print(item, " ")

    def predict(self,arr):
        for i in range(self.num_elements-1):
            if self.hypothesis[i] == None:
                pass
            elif self.hypothesis[i] != arr[i]:
                return 0
        return 1





