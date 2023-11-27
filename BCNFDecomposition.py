from ThreeNFSynthesis import getPrintMap
from AllCandidateKeys import findAllCandidateKeys
from CheckBCNF import checkBCNF
from FDRestriction import FDRestriction
from MinimalCover import findMinimalCover
from Utils import *

DecompositionMap = {}

def BCNFDecomposition(f, R, char):
    global DecompositionMap

    fd = checkBCNF(f, R)
    if fd is None:
        print('{0} => {1} is in BCNF\n'.format(char,getStringFromSet(R)))
        return True


    rSet = set(R)
    X, Y = fd
    print('{0} => {1} is not in BCNF due to {2} -> {3}'.format(char,getStringFromSet(R), X, Y))
    xClosure = computeClosure(f, set(X))
    print('Closure of X =>', getStringFromSet(xClosure))

    R1 = xClosure
    R2 = set(X).union(set(R) - xClosure)

    f1 = FDRestriction(f, list(getStringFromSet(R1)))
    f2 = FDRestriction(f, list(getStringFromSet(R2)))

    print('{0}1({1}) => ({2})'.format(char, getStringFromSet(R1), getPrintMap(f1, {val: val for val in getStringFromSet(R1)}, None, True)))
    print('{0}2({1}) => ({2})\n\n'.format(char, getStringFromSet(R2), getPrintMap(f2, {val: val for val in getStringFromSet(R2)}, None, True)))
    del DecompositionMap[getStringFromSet(R)]
    DecompositionMap[getStringFromSet(R1)] = f1
    DecompositionMap[getStringFromSet(R2)] = f2

    BCNFDecomposition(f1, list(getStringFromSet(R1)), char + '1')
    BCNFDecomposition(f2, list(getStringFromSet(R2)), char + '2')

if __name__ == "__main__":     
    f = set([('A', 'BCDEFGHIJ'), ('D', 'ABCDEFGHIJ'), ('EFI', 'G'), ('EI', 'H'), ('I', 'J'), ('G', 'EI')])
    R = list('ABCDEFGHIJ')
    DecompositionMap[getStringFromSet(R)] = f
    BCNFDecomposition(f, R, 'R')
    print(DecompositionMap)