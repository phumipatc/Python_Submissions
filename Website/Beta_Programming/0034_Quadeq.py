"""
	Task	: 0034_Quadeq
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 30 May 2021 [13:55]
	Algo	: 
	Status	: Finished
"""
def f(x):
	return [(i,x//i) for i in range(-abs(x),abs(x)+1) if i!=0 and x%i == 0]

A,B,C = [int(x) for x in input().split()]

ans = [(a,b,c,d) for a,c in f(A) for b,d in f(C) if a*d + b*c == B and a>0 and c>0]

if len(ans) == 0:	print('No Solution')
else:				print(' '.join([str(x) for x in min(ans)]))