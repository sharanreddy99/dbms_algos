from AllCandidateKeys import findAllCandidateKeys
from Utils import *

def NJTBD(f, R1, R2):
    left = R1.intersection(R2)

    right = R2 - R1
    if set(right).issubset(computeClosure(f, left)):
        return True
    
    right = R1 - R2
    if set(right).issubset(computeClosure(f, left)):
        return True
    
    return False

if __name__ == "__main__":     
    f = set([('AB', 'CDE'), ('CD', 'ABE'), ('E', 'D')])
    R1 = set('ACDE')
    R2 = set('BDF')
    print(NJTBD(f, R1, R2))