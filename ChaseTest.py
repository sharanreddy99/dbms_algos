# Check if the given relations are lossless or not
from AllCandidateKeys import findAllCandidateKeys
from Utils import *
from itertools import permutations
from copy import deepcopy

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
        print('\t'.join(R))
        for row in matrix:
            print('\t'.join(row))
        print()

    for newF in permutations(f):
        new_matrix = deepcopy(matrix)
        for X, Y in newF:
            unqTuples = {}
            for row in new_matrix:
                left = ''
                for char in X:
                    left += row[R.index(char)]

                for char in Y:
                    right += row[R.index(char)]

                if left in unqTuples:
                    if not left.isalpha():
                        old_right = unqTuples[left]
                        

                else:

                unqTuples[left] = right




    return True 

if __name__ == "__main__":     
    f = set([('A', 'B'), ('B', 'C'), ('CD', 'A')])
    RSet = [['A','D'], ['A','C'], ['B','C','D']]
    R = list('ABCD')
    print(chaseTest(f, RSet, R))