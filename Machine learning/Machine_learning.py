import LinearRegression as reg
import KNNAlgorythm as nn
import FindS as F
import numpy as np

def main():
 Fs = F.FindS()
 Fs.fit(Fs.exdata)
 Fs.printHypothesis()

 print(Fs.predict([1,3,2,1]))

main()