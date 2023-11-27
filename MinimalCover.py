from ExponentialProduct import printAll
from Utils import *



def findMinimalCover(f, R, char, isPrint=True):

    # Step 1
    Fc = f.copy()

    # Step 2 - Left Reduction
    if isPrint:
        print('left Reduction')
    while True:
        Fc = f.copy()
        for tup in Fc:
            A, B = tup
            for a in A:
                if len(set(A) - set(a)) != 0 and set(B).issubset(computeClosure(Fc, set(A) - set(a))):
                    f.remove((A, B))
                    f.add((getStringFromSet(set(A) - set(a)), B))

                    if Fc != f:
                        if isPrint:
                            printFD((A,B),(getStringFromSet(set(A) - set(a)), B), f, computeClosure(Fc, set(A) - set(a)))
                        break
                
            if Fc != f:
                break
        
        if Fc == f:
            break

    # Step 3 - Right Reduction
    if isPrint:
        print('\nRight Reduction')
    while True:
        Fc = f.copy()
        for tup in Fc:
            A, B = tup
            for b in B:
                newFc = Fc.copy()
                newFc.remove((A, B))
                newFc.add((A, getStringFromSet(set(B) - set(b))))
                if set(b).issubset(computeClosure(newFc, set(A))):
                    f.remove((A,B))
                    f.add((A, getStringFromSet(set(B) - set(b))))
                
                    if Fc != f:
                        if isPrint:
                            printFD((A,B),(A, getStringFromSet(set(B) - set(b))), f, computeClosure(newFc, set(A)))
                        break
            if Fc != f:
                break

        if Fc == f:
            break

    # Step 4 - If empty RHS, remove them
    if isPrint:
        print('Eliminating empty Fi')
    while True:
        Fc = f.copy()
        for tup in Fc:
            A, B = tup
            if B == "":
                f.remove((A,B))
                    
        if Fc == f:
            break
    if isPrint:
        printAll(f)

    if char == 'a':
        if isPrint:
            print('Standard or Decomposition Rule')
        # Step 5a - standard form or decommposition
        while True:
            Fc = f.copy()
            for tup in Fc:
                A, B = tup
                f.remove((A,B))
                for b in B:
                    f.add((A, b))
                    if len(B) > 1:
                        printFD((A,B), (A,b), f)
                        
            if Fc == f:
                break
    else:
        if isPrint:
            print('Non Standard or Union Rule')
        # Step 5b - non standard form or union
        H = f.copy()
        Fc = set()
        while True:
            Fc = f.copy()
            for tup1 in H:
                A, B = tup1
                G = set()
                X = set()
                for tup2 in Fc:
                    C, D = tup2

                    if set(A) == set(C):
                        G.add((C, D))
                        X.update(set(D))
                
                f = f - G
                f.add((A, getStringFromSet(X)))
            
            if Fc == f:
                break

    return f
            

if __name__ == "__main__":     
    #3A
    f = set([('A', 'B'), ('AB', 'C'), ('BC', 'DE'), ('AC', 'E'), ('DE', 'F')])
    R = ['A', 'B', 'C', 'D', 'E', 'F']
    char = 'b'

    #3B
    # f = set([('A', 'BC'), ('B', 'CDE'), ('C', 'E'), ('AD', 'BCE'), ('E', 'D')])
    # R = ['A', 'B', 'C', 'D', 'E']
    # char = 'a'

    #3C
    # f = set([('AB', 'C'), ('C', 'A'), ('BC', 'D'), ('ACD', 'B'), ('D', 'EG'), ('BE', 'C'), ('CG', 'BD'), ('CE', 'G')])
    # R = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    #char = 'b'


    resFd = findMinimalCover(f, R, char)
    printAll(resFd)