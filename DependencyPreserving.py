from Utils import *

def printSet(string, s):
	if len(s) == 0:
		print(string, 'φ')
	else:
		print(string, ''.join(list(s)))

def dependencyPreserving(f, RSet, R, isPrint = True):
	S = set()
	for X, Y in f:
		if isPrint:
			print('\nCurrent FD: %s->%s'%(X,Y))

		result = set(X)
		while True:
			oldResult = result.copy()
			idx = 1
			for customR in RSet:
				if isPrint:
					printSet('Old Result => ', result)
					printSet('R%s => '%(idx), customR)
					printSet('Result ∩ R%s => '%(idx),result.intersection(customR))
					printSet('Closure => ', computeClosure(f, result.intersection(customR)))
					printSet('Closure ∩ R%s => '%(idx),computeClosure(f, result.intersection(customR)).intersection(customR))
				C = computeClosure(f, result.intersection(customR)).intersection(customR)
				result.update(C)
				if isPrint:
					printSet('New result => ',result)
				print()

				idx += 1
			
			if oldResult == result:
				print('Old result is equal to new result\n')
				break
			else:
				print('Old result not equal to new result\n')
		
		print()
		printSet('Y => ', set(Y))
		printSet('result => ', result)
		printSet('Y ∩ result => ', result)
		if set(Y).intersection(result) != set(Y):
			print('FD: %s->%s is not preserved.'%(X,Y))
			return False
		print('------------------------------------------')
	return True

if __name__ == "__main__":     
	f = set([('A', 'B'), ('BC', 'D'), ('E', 'C'), ('D','A'), ('B','D')])
	RSet = [['A','B', 'C', 'D'], ['A','B', 'D', 'F']]
	R = list('ABCDEF')
	print('Hence the following decomposition is', ('preserving' if dependencyPreserving(f, RSet, R) else 'not preserving'))
	
