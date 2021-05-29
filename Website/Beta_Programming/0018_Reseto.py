"""
	Task	: 0018_Reseto
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 29 May 2021 [20:35]
	Algo	: 
	Status	: Finished
"""
N,K = [int(x) for x in input().split()]
seive = [False]*(N+1)
for i in range(2,N+1):
	if seive[i]:	continue
	# print(i,K)
	K-=1
	if K == 0:
		print(i)
		exit(0)
	for j in range(i*i,N+1,i):
		# print(j,K)
		K-= (1 if not(seive[j]) else 0)
		seive[j] = True
		if K == 0:
			print(j)
			exit(0)
