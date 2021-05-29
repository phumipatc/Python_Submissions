"""
	Task	: 0019_Perket
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 29 May 2021 [20:51]
	Algo	: 
	Status	: Finished
"""
N = int(input())
S = [0]*12
B = [0]*12
sumS = 1
sumB = 0
minn = int(1e9)
def permute(state:int,cnt:int):
	global sumS,sumB
	if state == N:
		if cnt == 0:	return 
		global minn
		minn = min(minn,int(abs(sumS-sumB)))
		return
	sumS*=S[state]
	sumB+=B[state]
	permute(state+1,cnt+1)
	sumS/=S[state]
	sumB-=B[state]
	permute(state+1,cnt)
for i in range(N):
	S[i],B[i] = [int(x) for x in input().split()]
permute(0,0)
print(minn)