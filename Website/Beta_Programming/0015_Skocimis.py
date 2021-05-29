"""
	Task	: 0015_Skocimis
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 29 May 2021 [22:09]
	Algo	: 
	Status	: Finished
"""
A,B,C = [int(x) for x in input().split()]
print(max(B-A-1,C-B-1))