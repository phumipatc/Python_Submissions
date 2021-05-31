"""
	Task	: 0040_Prime-Odd
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 31 May 2021 [12:21]
	Algo	: 
	Status	: Finished
"""
N = int(input())
for i in range(N):
	num = int(input())
	if num == 2 or num%2:	print('T')
	else:					print('F')