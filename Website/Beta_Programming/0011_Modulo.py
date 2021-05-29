"""
	Task	: 0011_Modulo
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 29 May 2021 [22:09]
	Algo	: 
	Status	: Finished
"""
s = set()
for i in range(10):
	s.add(int(input())%42)
print(len(s))