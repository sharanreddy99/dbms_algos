# Check if the given relations are lossless or not
from AllCandidateKeys import findAllCandidateKeys
from Utils import *
from itertools import permutations
from copy import deepcopy

def areMatricesSame(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            if mat1[i][j] != mat2[i][j]:
                return False
    
    return True

def iterative(matrix, f):
    isSecondTimeUnchanged = None
    idx = 1
    while True:
        new_matrix = deepcopy(matrix)
        isChanged = False

        for X, Y in f:
            unqTuples = {}
            for row in new_matrix:
                left = ''
                for char in X:
                    left += row[R.index(char)]

                right = row[R.index(Y)]

                if left in unqTuples:
                    if (unqTuples[left]) != 1 and len(right) == 1:
                        unqTuples[left] = right
                else:
                    unqTuples[left] = right

            for row in new_matrix:
                left = ''
                for char in X:
                    left += row[R.index(char)]

                right = row[R.index(Y)]
                if len(row[R.index(right[0].upper())]) != 1:
                    row[R.index(right[0].upper())] = unqTuples[left]
            
            if not (areMatricesSame(matrix, new_matrix)):
                print('Step {2}: After applying FD {0}->{1}, matrix is: '.format(X, Y, idx))
                idx += 1
                printMatrix(new_matrix)
                matrix = deepcopy(new_matrix)
                isChanged =True
                isSecondTimeUnchanged = None
            else:
                isChanged = False

        if not isChanged:
            if isSecondTimeUnchanged is None:
                print('No changes testing all the FDs once')
                isSecondTimeUnchanged = True
            else:
                return new_matrix
    
        
def printMatrix(matrix):
    print('\t'.join(R))
    for row in matrix:
        print('\t'.join(row))
    print()

def chaseTest(f, RSet, R, isPrint = True):
    matrix = []
    for i in range(len(RSet)):
        temp = []
        for char in R:
            temp.append(char.lower() + str(i + 1))
        matrix.append(temp)
    
    for i in range(len(RSet)):
        for char in RSet[i]:
            matrix[i][R.index(char)] = char.lower()

    if isPrint:
        printMatrix(matrix)

    new_matrix = iterative(matrix, f)
    return True if any([all([len(char) == 1 for char in row]) for row in new_matrix]) else False

if __name__ == "__main__":     
    # f = list([('A', 'B'), ('BC', 'D'), ('E', 'C'), ('D', 'A'), ('D', 'E'), ('C', 'F')])
    # RSet = [['A','C'], ['A','B', 'D'], ['D','E','F'], ['C', 'F']]
    # R = list('ABCDEF')
    f = list([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'D')])
    RSet = [['A','B'], ['B', 'C'],['C','D']]
    R = list('ABCD')
    print(chaseTest(f, RSet, R))