"""
	Task	: 0020_Pet
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 29 May 2021 [22:05]
	Algo	: 
	Status	: Finished
"""
maxx = idx = 0
for i in range(5):
	num = [int(x) for x in input().split()]
	all = sum(num)
	if(all>maxx):
		maxx = all;
		idx = i
print(idx+1,maxx)