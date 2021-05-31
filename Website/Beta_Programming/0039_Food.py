"""
	Task	: 0039_Food
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 31 May 2021 [11:41]
	Algo	: 
	Status	: Finished
"""
import itertools as itt
N = int(input())
M = int(input())
forbidden = [int(x) for x in input().split()]
ans = [x for x in itt.permutations(range(1,N+1),N) if x[0] not in forbidden]
for x in ans:
	print(' '.join([str(y) for y in x]))