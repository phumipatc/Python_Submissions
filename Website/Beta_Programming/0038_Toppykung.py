"""
	Task	: 0038_Toppykung
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 31 May 2021 [11:19]
	Algo	: 
	Status	: Finished
"""
N = int(input())
mp = dict()
for i in range(N):
	inp = input()
	mp[inp] = 1
for x in sorted(mp):
	print(x)