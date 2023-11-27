from AllCandidateKeys import findAllCandidateKeys
from Utils import *

def check3NF(f, R):
    S = set()
    for X, Y in f:
        set_X = set(X)
        set_Y = set(Y)

        if not (set_Y.issubset(set_X) or set_Y == set_X) and computeClosure(f, set_X) != set(R):
            S.update([(X, Y)])
        
    if len(S) == 0:
        return True
    
    K = findAllCandidateKeys(f, R, False)
    PrimeAttributes = set()
    for C in K:
        PrimeAttributes.update(C)
    
    for X, Y in S:
        set_X = set(X)
        set_Y = set(Y)
        for A in set_Y - set_X:
            if A not in PrimeAttributes:
                print('for {0}->{1}, {2} is not in the set of prime attributes {3}'.format(X, Y, 'Y-X: {0}'.format(A), getStringFromSet(PrimeAttributes)))
                return False
    
    return True 

if __name__ == "__main__":     
    f = set([('AB', 'CDE'), ('CD', 'ABE'), ('E', 'D')])
    R = list('ABCDE')
    print(check3NF(f, R))