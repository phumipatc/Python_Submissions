"""
	Task	: 0036_Activity
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 30 May 2021 [17:06]
	Algo	: 
	Status	: Finished
"""
import math
N = int(input())
N+=(N%2)
ans = 1
for i in range(N//2+1,N+1):
	ans*=i
for i in range(1,N//2+1):
	ans//=i
print(ans)
# print(math.comb(N,N//2))
