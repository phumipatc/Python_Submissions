"""
	Task	: 0013_Seven_Dwarves
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 29 May 2021 [22:09]
	Algo	: 
	Status	: Finished
"""
num = list()
sum = 0
for i in range(9):
	num.append(int(input()))
	sum+=num[i]
for i in range(9):
	for j in range(9):
		if i == j:	continue
		if sum-num[i]-num[j] == 100:
			for k in range(9):
				if k == i or k == j:	continue
				print(num[k])
			break