
from functools import cmp_to_key
from itertools import chain, combinations

def computeClosure(fd, c):
    closure = c.copy()
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


def getStringFromSet(s):
    return "".join(list(sorted(s)))



def printFD(oldFD, newFD, f, closure = None):
    print('oldFD', oldFD)
    print('newFD', newFD)
    if closure is not None:
        print('Closure', getStringFromSet(closure))
    print('Updated FDs => ( {0} )'.format(', '.join(['%s -> %s'%(u, v) for u,v in f])))
    print()

def customCompare(x, y):
    if len(x) != len(y):
        return len(x) - len(y)
    else:
        if x < y:
            return -1
        if x == y:
            return 0
        if x > y:
            return 1

def getPowerSet(R):
    res = list(sorted(tuple(chain.from_iterable(combinations(R, x) for x in range(1, len(R)+1)))))
    res = [tuple(sorted(val)) for val in res]
    res = list(sorted(res, key=cmp_to_key(customCompare)))
    return res
    

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
    print(s)
    return s

def extractLHS(Fds):
    s = set()
    for tup in Fds:
        u, _  = tup
        s.update(set(u))
    
    return s


def extractRHS(Fds):
    s = set()
    for tup in Fds:
        _, v  = tup
        s.update(set(v))
    
    return s

def printPowerSet(ps):
    print('\nPower Set: ')
    for p in ps:
        print(''.join(p), end=',')
    print('\n\n')