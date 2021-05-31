"""
	Task	: 0033_Looblike
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 30 May 2021 [11:58]
	Algo	: 
	Status	: Finished
"""
N = int(input())
num = [int(x) for x in input().split()]
mapp = dict()
for x in num:
	if x in mapp:	mapp[x]+=1
	else:			mapp[x] = 1
maxx = max([x for x in mapp.values()])
for x in sorted(mapp):
	if mapp[x] == maxx:
		print(x,end=' ')