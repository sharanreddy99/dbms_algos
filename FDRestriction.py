from AllCandidateKeys import findAllCandidateKeys
from MinimalCover import findMinimalCover
from Utils import *

def FDRestriction(f, S):
    Fs = set()
    for X in getPowerSet(S):
        xClosure = computeClosure(f, set(X)).intersection(S)
        if set(X).issubset(xClosure) and set(X) != xClosure:
            Fs.update([(getStringFromSet(X), getStringFromSet(xClosure - set(X)))])
    
    Fc = findMinimalCover(Fs, S, None, False)
    return Fc


if __name__ == "__main__":     
    f = set([('A', 'C'), ('CE', 'AD'), ('CD', 'E')])
    R = list('ACDE')
    print(FDRestriction(f, R))