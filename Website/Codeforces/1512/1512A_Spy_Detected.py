"""
	Task	: 1512A_Spy_Detected
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 04 July 2021 [23:44]
	Algo	: BF
	Status	: 
"""
Q = int(input())
while(Q):
	Q-=1
	N = int(input())
	a = [int(x) for x in input().split()]
	ans = 0
	for i in range(1,N-1):
		if a[i] != a[i-1] and a[i] != a[i+1]:
			ans = i+1
			break
	if ans:
		print(ans)
		continue
	if a[0]!=a[1]:	ans = 1
	else:			ans = N
	print(ans)