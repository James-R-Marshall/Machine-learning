import numpy as np
class CandElim :
    """"This algorithm is similar to the FindS algorithm, it finds all the possible hypothesis's that can be found instead of just one. This is done by converging a specific hyp with general hyps """
    index = 0
    num_elements = 0
    num_samples = 0
    hyp = None;
    Ghyp = None;
    exdata = (      [1, 3, 2, 1, 1],
                    [1, 3, 1, 3, 0],
                    [2, 3, 2, 1, 1],
                    [2, 2, 2, 3, 1])

    def fit(self, arr):
        x = 0
        y = 0
        z = 0
        num_genList = 1
        shp = np.shape(arr)
        self.num_elements = shp[1]
        self.num_samples = shp[0]
        
        while arr[self.index][self.num_elements - 1] == 0:
            self.index+=1
        self.hyp = arr[self.index]
        self.Ghyp = [[None]* (self.num_elements - 1)]
        for x in range(self.num_samples):
            if arr[x][self.num_elements - 1] == 1 :
                y = 0
                for y in range (self.num_elements - 1):
                    z = 0
                    if arr[x][y] != self.hyp[y]:
                        for row in self.Ghyp:
                            if row[y] == self.hyp[y]:
                                if self.Ghyp[z][y] != None:
                                    self.Ghyp.pop(z)
                                   
                                    z-=1
                            z+=1
                        self.hyp[y] = None

            else:
                for y in range(self.num_elements - 1):
                    if arr[x][y] != self.hyp[y]:
                        pass
                    else:
                        num_genList+=1
                        T = [None]*(self.num_elements - 1)
                        T[y] = arr[x][y]
                        self.Ghyp.append(T)
        return self.hyp

