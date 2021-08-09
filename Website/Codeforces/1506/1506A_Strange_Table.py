"""
	Task	: 1506A_Strange_Table
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 04 July 2021 [23:05]
	Algo	: Math
	Status	: 
"""
Q = int(input())
while(Q):
	Q-=1
	n,m,x = [int(x) for x in input().split()]
	i = (x-1)%n
	j = (x-1)//n
	# print(i,j)
	print(i*m + j + 1)