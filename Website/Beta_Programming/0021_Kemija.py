"""
	Task	: 0021_Kemija
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 30 May 2021 [09:51]
	Algo	: 
	Status	: Finished
"""
inp = input()
vowels = ['a','e','i','o','u']
mes = []
for x in inp:
	mes.append(x)
ans = []
i = 0
while i<len(mes):
	if i>0 and i<len(mes)-1:
		if mes[i] == 'p' and mes[i-1] == mes[i+1] and vowels.count(mes[i-1]):
			mes[i+1] = '0'
			i+=1
		else:
			ans.append(mes[i])
	else:
		ans.append(mes[i])
	i+=1
for x in ans:
	print(x,end='')