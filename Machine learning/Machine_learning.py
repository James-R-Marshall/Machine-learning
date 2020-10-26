import LinearRegression as reg
import KNNAlgorythm as nn
import FindS as F
import CandidateElimination as CE
import numpy as np

def main():
    Can = CE.CandElim()
    print(Can.fit(Can.exdata))
    
main()