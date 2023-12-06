from AllCandidateKeys import findAllCandidateKeys
from MinimalCover import findMinimalCover
from ThreeNFSynthesis import getPrintMap
from Utils import *

def FDRestriction(f, S, isPrint =True):
    Fs = set()
    for X in getPowerSet(S):
        xClosure = computeClosure(f, set(X)).intersection(S)
        if set(X).issubset(xClosure) and set(X) != xClosure:
            if isPrint:
                print('{0} ⊂ {1}'.format(getStringFromSet(X), getStringFromSet(xClosure)))
            Fs.update([(getStringFromSet(X), getStringFromSet(xClosure - set(X)))])
        else:
            if isPrint:
                # print('{0} ⊄ {1}'.format(getStringFromSet(X), getStringFromSet(xClosure)))
                pass

    if isPrint:
        print('Fs => ({0})\n'.format(', '.join(getPrintMap(Fs, {val: val for val in S}, None, True))))
        print('Minimal Cover:\n--------------')
    Fc = findMinimalCover(Fs, S, None, isPrint)
    return Fc


if __name__ == "__main__":     
    #f = set([('CD', 'E'), ('B', 'C'), ('AB', 'CDE')])
    f = set([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D','B')])
    R = list('BD')
    print(FDRestriction(f, R))