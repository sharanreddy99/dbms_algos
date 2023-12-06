from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys
import os

from MinimalCover import findMinimalCover
from AllCandidateKeys import findAllCandidateKeys
from BCNFDecomposition import *
from ChaseTest import chaseTest
from Check3NF import check3NF
from DependencyPreserving import dependencyPreserving
from ExponentialProduct import findFDs
from NonAdditiveTestBinDecomposition import NJTBD
from ThreeNFSynthesis import ThreeNFSynthesis, printSetMap


app = Flask(__name__)
CORS(app, support_credentials=True)

# Helpers
def changeStdOut():
    open('output.out', 'w').close()
    f = open('output.out', 'a')
    sys.stdout = f
    return f

def fetchStdOut():
    return "".join(open('output.out', 'r').readlines())


@app.route("/", methods=["GET","POST"])
@cross_origin(supports_credentials=True)
def healthcheck():
    return 'The server is alive'

@app.route("/run_algo", methods=["POST"])
@cross_origin(supports_credentials=True)
def run_algo():
    fp = changeStdOut()

    data = request.get_json()
    if os.getenv('DBMS_ALGOS_PASSWORD') != data['password']:
        return 'Cannot run this algorithm'
    

    f = set(map(lambda x: tuple(x.split(data['sideSeparator'])), data['f'].split(data['fdSeparator'])))
    R = list(data['R'])
    RSet = list(map(lambda x: list(x), data['RSet'].split(data['fdSeparator'])))
    char = data['char']
    
    try:
        match data['type']:
            case 'all_candidate_keys':
                findAllCandidateKeys(f, R)
            case 'bcnf_decomposition':
                DecompositionMap[getStringFromSet(R)] = f
                BCNFDecomposition(f, R, 'R')
                printDecompositionMap(DecompositionMap)
            case 'chase_test':
                print(chaseTest(f, RSet, R))
            case 'check_3nf':
                print(check3NF(f, R))
            case 'check_bcnf':
                res = checkBCNF(f, R)
                print(True if res == None else False)
            case 'dependency_preserving':
                print('Hence the following decomposition is', ('preserving' if dependencyPreserving(f, RSet, R) else 'not preserving'))
            case 'exponential_product':
                rPowerSet = getPowerSet(R)
                countFds = findFDs(f, R, rPowerSet)
                printAll(countFds)
                print('Count => ',len(countFds))
            case 'fd_restriction':
                print(FDRestriction(f, R))
            case 'minimal_cover':
                resFd = findMinimalCover(f, R, char)
                printAll(resFd)
            case 'non_additive_test_bin_decomposition':
                R1 = set(RSet[0])
                R2 = set(RSet[1])
                print(NJTBD(f, R1, R2))
            case '3nf_synthesis':
                customMap = {val: val for val in R}
                res1, res2 = ThreeNFSynthesis(f, R, customMap)

                print('\nStep 5: The resulting decompositions are: ')
                for i in range(len(res1)):
                    print('R%s => '%(i + 1),end='')
                    printSetMap(res1[i], customMap, True)
                    print('F{0} => ( {1} )'.format(i+ 1, ', '.join(getPrintMap(res2[i], customMap, None, True))))
                    print()
    except:
        print('Exception Occured')

    fp.flush()
    data = fetchStdOut()

    return data