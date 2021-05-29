"""
	Task	: 0016_Ptice
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 29 May 2021 [16:54]
	Algo	: 
	Status	: Finished
"""
n = int(input())
ans = input()
adrian = 'ABC'*35
bruno = 'BABC'*30
goran = 'CCAABB'*20
A = B = G = 0
for i in range(n):
	if ans[i] == adrian[i]:	A+=1
	if ans[i] == bruno[i]:	B+=1
	if ans[i] == goran[i]:	G+=1
maxx = max(A,B,G)
print(maxx)
if maxx == A:
	print('Adrian')
if maxx == B:
	print('Bruno')
if maxx == G:
	print('Goran')
