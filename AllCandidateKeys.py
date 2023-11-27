from inspect import getclosurevars
from Utils import *

def findAllCandidateKeys(f, R, isPrint = True):
    LHS = extractLHS(f)
    RHS = extractRHS(f)
    setR = set(R)
    
    # Step 1
    ignoreR = setR - (LHS.union(RHS))
    if isPrint:
        print('Step1: IgnoreNeither => ', ignoreR)

    # Step 2
    leftOnlyR = LHS - RHS
    if isPrint:
        print('Step2: LeftOnlyR => ', leftOnlyR)

    
    # Step 3
    rightOnlyR = RHS - LHS
    if isPrint:
        print('Step3: RightOnlyR => ', rightOnlyR)

    #Step 4
    combineStep1Step2R = ignoreR.union(leftOnlyR)
    if isPrint:
        print('Step4: CombineStep1Step2 => ', combineStep1Step2R)

    # Step 5
    if isPrint:
        print('Step-5: Closure of',getStringFromSet(combineStep1Step2R),'is', getStringFromSet(computeClosure(f, combineStep1Step2R)))
    if setR == computeClosure(f, combineStep1Step2R):
        if isPrint:
            print('CandidateKeys fetched =>  ', getStringFromSet(combineStep1Step2R))
        return [getStringFromSet(combineStep1Step2R)]
    else:
        resCandidateSet = set()
        # Step 6
        bothR = LHS.intersection(RHS)
        if isPrint:
            print('Step 6: Both R => ', bothR)
        bothRPowerSet = getPowerSet(bothR)
        if isPrint:
            printPowerSet(bothRPowerSet)

        # Step 7
        if isPrint:
            print('Step 7')
        for tup in bothRPowerSet:
            psSet = "".join(tup)
            newAttrList = set(combineStep1Step2R)
            newAttrList.update(set(psSet))
            if computeClosure(f, set(newAttrList)) == setR:
                for tup in resCandidateSet:
                    if newAttrList.issubset(set(tup)):
                        resCandidateSet.remove(tup)
                        resCandidateSet.add(getStringFromSet(newAttrList))     
                        break
                    elif set(tup).issubset(newAttrList):
                        if isPrint:
                            print('%s+ = %s is a subset of %s but a smaller sized candidate %s is already present'%(getStringFromSet(newAttrList), getStringFromSet(computeClosure(f, set(newAttrList))), 'R', tup))
                        break
                else:
                    if isPrint:
                        print('%s+ = %s is a subset of %s'%(getStringFromSet(newAttrList), getStringFromSet(computeClosure(f, set(newAttrList))), 'R'))
                    resCandidateSet.add(getStringFromSet(newAttrList))     
            else:
                if isPrint:
                    print('%s+ = %s is not a subset of %s'%(getStringFromSet(newAttrList), getStringFromSet(computeClosure(f, set(newAttrList))), 'R'))
         
            
        return resCandidateSet
            

if __name__ == "__main__":     
    #4A
    f = set([('CD', 'AE'), ('A', 'C'), ('CE', 'D')])
    R = list('ACDE')

    #4B
    # f = set([('AB', 'C'), ('CD', 'F'), ('F', 'A'), ('CE', 'D')])
    # R = ['A', 'B', 'C', 'D', 'E', 'F']

    # Lecture Example
    # f = set([('DF', 'C'), ('BC', 'F'), ('E', 'A'), ('ABC', 'E')])
    # R = ['A','B','C','D','E','F']

    resAttrList = findAllCandidateKeys(f, R)
    print(resAttrList)