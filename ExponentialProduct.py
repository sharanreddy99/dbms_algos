from re import L
from itertools import chain, combinations

def getPowerSet(R):
    return chain.from_iterable(combinations(R, x) for x in range(1, len(R)+1))

def printRound(roundNumber, roundName, f):
    print('Round ',roundNumber, roundName)
    for tup in f:
        u, v = tup
        print(u, '->', v)
    print('number of FDs', len(f))
    print()

def printAll(f):
    s = ''
    for tup in f:
        u, v = tup
        s += ' %s -> %s,'%(u, v)
    return s


def findFDs(f, R, rPowerSet):
    idx = 1

    while True:
        oldF = f.copy()
        if idx == 1:
            for u in R:
                f.add((u, u))

        else: 
            # reflexivity rule
            for tup in oldF:
                u, v = tup
                for j in range(len(v)):
                    f.add((u, v[: j + 1]))
        printRound(idx, 'Reflexivity Rule', f - oldF)

        temp1F = f.copy()     
        # augmentation rule
        for augTuple in rPowerSet:
            for tup in oldF:
                u, v = tup
                newU = "".join(list(sorted(set(u).union(set(augTuple)))))
                newV = "".join(list(sorted(set(v).union(set(augTuple)))))
                f.add((newU, newV))

        printRound(idx, 'Augmentation Rule', f - temp1F)

        tempF = f.copy()  
        for tup1 in tempF:
            l1, r1 = tup1
            for tup2 in tempF:
                l2, r2 = tup2
                if l1 == l2 and r1 == r2:
                    continue
            
                if r1 == l2:
                    f.add((l1, r2))
        
        printRound(idx, 'Transitivity Rule', f - tempF)

        if f == oldF:
            break
        else:
            
            idx += 1
    
    return f


if __name__ == "__main__":
    f = set([('A', 'B')])
    R = ['A', 'B', 'C']
    rPowerSet = getPowerSet(R)
    print(printAll(findFDs(f, R, rPowerSet)))