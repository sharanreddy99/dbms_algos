#3A
#f = set([('A', 'B'), ('AB', 'C'), ('BC', 'DE'), ('AC', 'E'), ('DE', 'F')])
#R = ['A', 'B', 'C', 'D', 'E', 'F']
#5B

#3B
# f = set([('A', 'BC'), ('B', 'CDE'), ('C', 'E'), ('AD', 'BCE'), ('E', 'D')])
# R = ['A', 'B', 'C', 'D', 'E']
#5A

#3C
f = set([('AB', 'C'), ('C', 'A'), ('BC', 'D'), ('ACD', 'B'), ('D', 'EG'), ('BE', 'C'), ('CG', 'BD'), ('CE', 'G')])
R = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#5B


# char = input('Enter step: a or b? ')
char = 'a'

def getStringFromSet(s):
    return "".join(list(sorted(s)))


def computeClosure(fd, closure):
    changed = True
    while changed:
        changed = False

        for tup in fd:
            left, right = tup
            left = set(left)
            right = set(right)

            if left.issubset(closure) and not right.issubset(closure):
                closure.update(right)
                changed = True

    return closure

# Step 1
Fc = f.copy()

# Step 2 - Left Reduction
while True:
    Fc = f.copy()
    for tup in Fc:
        A, B = tup
        for a in A:
            if len(set(A) - set(a)) != 0 and set(B).issubset(computeClosure(Fc, set(A) - set(a))):
                f.remove((A, B))
                f.add((getStringFromSet(set(A) - set(a)), B))

                if Fc != f:
                    break
            
        if Fc != f:
            break
    
    if Fc == f:
        break

# Step 3 - Right Reduction
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
                    break
        if Fc != f:
            break

    if Fc == f:
        break

# Step 4 - If empty RHS, remove them
while True:
    Fc = f.copy()
    for tup in Fc:
        A, B = tup
        if B == "":
            f.remove((A,B))
                
    if Fc == f:
        break

if char == 'a':
    # Step 5a - standard form or decommposition
    while True:
        Fc = f.copy()
        for tup in Fc:
            A, B = tup
            f.remove((A,B))
            for b in B:
                f.add((A, b))
                    
        if Fc == f:
            break
else:
    # Step 5b - non standard form or union
    H = f.copy()
    Fc = set()
    while True:
        Fc = f.copy()
        for tup1 in Fc:
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

print(f)
        