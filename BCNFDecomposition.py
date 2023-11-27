from ThreeNFSynthesis import getPrintMap, printMap
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
    print('{0} => {1} is not in BCNF due to {2} -> {3} as the FD is not trivial and closure of {4} != {5}'.format(char,getStringFromSet(R), X, Y, X, char))
    xClosure = computeClosure(f, set(X))
    print('Closure of {0} => {1}'.format(X, getStringFromSet(xClosure)))

    R1 = xClosure
    R2 = set(X).union(set(R) - xClosure)

    print('FD Restriction for f{0}:\n--------------------'.format(char[1:] + '1'))
    f1 = FDRestriction(f, list(getStringFromSet(R1)))
    print('{0}1({1}) => ({2})\n'.format(char, getStringFromSet(R1), ', '.join(getPrintMap(f1, {val: val for val in getStringFromSet(R1)}, None, True))))
    print('FD Restriction for f{0}:\n--------------------'.format(char[1:] + '2'))
    f2 = FDRestriction(f, list(getStringFromSet(R2)))
    print('{0}2({1}) => ({2})\n\n'.format(char, getStringFromSet(R2), ', '.join(getPrintMap(f2, {val: val for val in getStringFromSet(R2)}, None, True))))

    del DecompositionMap[getStringFromSet(R)]
    DecompositionMap[getStringFromSet(R1)] = f1
    DecompositionMap[getStringFromSet(R2)] = f2

    BCNFDecomposition(f1, list(getStringFromSet(R1)), char + '1')
    BCNFDecomposition(f2, list(getStringFromSet(R2)), char + '2')

def printDecompositionMap(d):
    idx = 1
    for key in d:
        print('R{0} => {1}\nF{2} => ({3})\n'.format(idx, key,idx,', '.join(getPrintMap(d[key], {val: val for val in key}, None, True))))
        idx += 1
    

if __name__ == "__main__":     
    f = set([('AB', 'CD'), ('D', 'E'), ('A', 'C'), ('B', 'D')])
    R = list('ABCDE')
    DecompositionMap[getStringFromSet(R)] = f
    BCNFDecomposition(f, R, 'R')
    printDecompositionMap(DecompositionMap)