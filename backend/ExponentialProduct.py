from Utils import *


def findFDs(f, R, rPowerSet, isPrint = True):
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
                for pSet in getPowerSet(list(v)):
                    if set(pSet).issubset(set(u)):
                        f.add((u, getStringFromSet(pSet)))

        if isPrint:
            printRound(idx, 'Reflexivity Rule', f - oldF)

        temp1F = f.copy()     
        # augmentation rule
        for augTuple in rPowerSet:
            for tup in oldF:
                u, v = tup
                newU = "".join(list(sorted(set(u).union(set(augTuple)))))
                newV = "".join(list(sorted(set(v).union(set(augTuple)))))
                f.add((newU, newV))

        if isPrint:
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
        
        if isPrint:
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
    countFds = findFDs(f, R, rPowerSet)
    printAll(countFds)
    print('Count => ',len(countFds))
