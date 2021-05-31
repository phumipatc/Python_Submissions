"""
	Task	: 0029_Frog
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 30 May 2021 [11:46]
	Algo	: 
	Status	: Finished
"""
M,N = [int(x) for x in input().split()]
if M>N:	print(2)
else:	print((N+M-1)//M)