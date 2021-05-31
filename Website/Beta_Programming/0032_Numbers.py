"""
	Task	: 0032_Numbers
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 30 May 2021 [11:49]
	Algo	: 
	Status	: Finished
"""
N = int(input())
num = sorted([int(x) for x in input().split()])
for i in range(len(num)):
	if not(num[i]):	continue
	num[0],num[i] = num[i],num[0]
	break;
print(''.join([str(x) for x in num]))