from AllCandidateKeys import findAllCandidateKeys
from MinimalCover import findMinimalCover
from Utils import *

def printSet(string, s):
	if len(s) == 0:
		print(string, 'φ')
	else:
		print(string, ''.join(list(s)))


def printMap(f, map, char):
	idx = 1
	for X, Y in f:
		new_set_X = set([map[char] for char in list(sorted(X))])
		new_set_Y = set([map[char] for char in list(sorted(Y))])
		if char != None:
			print('%s%s: '%(char, idx),new_set_X,'->', new_set_Y)
		else:
			print(new_set_X, '->', new_set_Y)
		idx += 1
	print()

def printSetMap(s, map):
	print('{',','.join([map[char] for char in list(sorted(list(s)))]),'}')


def ThreeNFSynthesis(f, R, isPrint = True):
	# step 1
	min_cover = findMinimalCover(f, R, 'b', False)
	if isPrint:
		print('Step 1: Minimal cover generation')
		printMap(min_cover, map, 'f')

	# step 2
	if isPrint:
		print('\nStep 2: Generation of relation schemas')
	RSet = []
	FSet = []
	idx = 1
	for X, Y in min_cover:
		RSet.append(set(X).union(set(Y)))
		if isPrint:
			print('R%s -> '%(idx), RSet[-1])

		currF = []
		for A, B in min_cover:
			D = set(B).intersection(RSet[-1])
			temp = RSet[-1].intersection(D)
			if (set(A).issubset(RSet[-1]) or set(A) == RSet[-1]) and len(D) > 0 and D == set(B).intersection(RSet[-1]):
				currF.append((A, getStringFromSet(D)))

		if len(currF) > 0:
			FSet.append(currF)
			print('F%s: '%(idx))
			printMap(currF, map, None)

		idx += 1
		
	# step 3
	print('Step 3: Check if schema contains a candidate key')
	K = list(findAllCandidateKeys(min_cover, R, False))
	i = 0
	found = False
	
	while not found and i < len(K):
		j = 0
		while not found and j < len(FSet):
			if set(K[i]).issubset(RSet[j]) or set(K[i]) == RSet[j]:
				found = True
			else:
				j += 1
		
		if not found:
			i += 1
	
	if not found:
		FSet.append([])
		RSet.append(set(K[0]))

	# Step 4
	print('Step 4: Test for containment relationships between schemas')
	vis = [False for i in range(len(RSet))]
	for i in range(len(RSet)):
		for j in range(len(RSet)):
			if i == j:
				continue
				
			if RSet[i].issubset(RSet[j]) or RSet[i] == RSet[j]:
				vis[i] = True
				print('R%s is a subset of R%s'%(i + 1, j  + 1))
				break
	
	res1, res2 = [], []
	for i in range(len(RSet)):
		if not vis[i]:
			res1.append(RSet[i])
			res2.append(FSet[i])
	
	return res1, res2

if __name__ == "__main__":     
	# f = set([('A', 'BCDEFG'), ('D', 'A'), ('EFG', 'H'), ('EG','I'),('G','J'), ('H', 'EG')])
	# map = {'A': 'persid', 'B': 'name', 'C': 'rank', 'D': 'room', 'E': 'city', 'F': 'street', 'G': 'state', 'H': 'zipcode', 'I': 'area-code', 'J': 'government'}

	f = set([('A', 'BC'), ('CD', 'AE'), ('ABD', 'CD'), ('CE','AD')])
	map = {val: val for val in 'ABCDE'}
	R = list('ABCDE')

	res1, res2 = ThreeNFSynthesis(f, R)

	print('\nStep 5: Return the decomposition')
	for i in range(len(res1)):
		print('R%s => '%(i + 1),end='')
		printSetMap(res1[i], map)
		print('F%s: '%(i+ 1))
		printMap(res2[i], map, None)
		print()
