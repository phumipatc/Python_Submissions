"""
	Task	: 0017_Kornislav
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 29 May 2021 [20:33]
	Algo	: 
	Status	: Finished
"""
num = [int(x) for x in input().split()]
num.sort()
print(num[0]*num[2])