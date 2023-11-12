from inspect import getclosurevars
from Utils import *

def findAllCandidateKeys(f, R):
    LHS = extractLHS(f)
    RHS = extractRHS(f)
    setR = set(R)
    
    # Step 1
    ignoreR = setR - (LHS.union(RHS))
    print('Step1: IgnoreNeither => ', ignoreR)

    # Step 2
    leftOnlyR = LHS - RHS
    print('Step2: LeftOnlyR => ', leftOnlyR)

    
    # Step 3
    rightOnlyR = RHS - LHS
    print('Step3: RightOnlyR => ', rightOnlyR)

    #Step 4
    combineStep1Step2R = ignoreR.union(leftOnlyR)
    print('Step4: CombineStep1Step2 => ', combineStep1Step2R)

    # Step 5
    if setR == computeClosure(f, combineStep1Step2R):
        print('Step5: CandidateKeys fetched =>  ', combineStep1Step2R)
        return combineStep1Step2R
    else:
        resCandidateSet = set()
        # Step 6
        bothR = LHS.intersection(RHS)
        print('Step 6: Both R => ', bothR)
        bothRPowerSet = getPowerSet(bothR)
        printPowerSet(bothRPowerSet)

        # Step 7
        print('Step 7')
        for tup in bothRPowerSet:
            psSet = "".join(tup)
            newAttrList = set(combineStep1Step2R)
            newAttrList.update(set(psSet))
            print(getStringFromSet(newAttrList), computeClosure(f, set(newAttrList)))
            if computeClosure(f, set(newAttrList)) == setR:
                for tup in resCandidateSet:
                    if newAttrList.issubset(set(tup)):
                        resCandidateSet.remove(tup)
                        resCandidateSet.add(getStringFromSet(newAttrList))     
                        break
                    elif set(tup).issubset(newAttrList):
                        break
                else:
                    resCandidateSet.add(getStringFromSet(newAttrList))     
                        
            
        return resCandidateSet
            

if __name__ == "__main__":     
    #4A
    f = set([('B', 'CE'), ('E', 'FH'), ('BC', 'H'), ('CD', 'A'), ('A', 'DG'), ('H', 'BCE'), ('H', 'G')])
    R = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    #4B
    # f = set([('AB', 'C'), ('CD', 'F'), ('F', 'A'), ('CE', 'D')])
    # R = ['A', 'B', 'C', 'D', 'E', 'F']

    # Lecture Example
    # f = set([('DF', 'C'), ('BC', 'F'), ('E', 'A'), ('ABC', 'E')])
    # R = ['A','B','C','D','E','F']

    resAttrList = findAllCandidateKeys(f, R)
    print(resAttrList)