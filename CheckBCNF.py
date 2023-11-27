from AllCandidateKeys import findAllCandidateKeys
from Utils import *

def checkBCNF(f, R):
    S = set()
    for X, Y in f:
        set_X = set(X)
        set_Y = set(Y)

        if not (set_Y.issubset(set_X) or set_Y == set_X) and computeClosure(f, set_X) != set(R):
            return False
        
    return True 

if __name__ == "__main__":     
    f = set([('AB', 'C'), ('C', 'B')])
    R = ['A', 'B', 'C', 'D']
    print(checkBCNF(f, R))