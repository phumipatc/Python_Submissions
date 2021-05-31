"""
	Task	: 0035_Bigtriangle
	Author	: Phumipat C. [MAGCARI]
	Language: Python
	Created	: 30 May 2021 [14:00]
	Algo	: 
	Status	: Finished
"""
import itertools
def area(A):
	x1,y1 = A[0][0],A[0][1]
	x2,y2 = A[1][0],A[1][1]
	x3,y3 = A[2][0],A[2][1]
	return round(abs(x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1)/2,3)

N = int(input())
point = [[int(x) for x in input().split()] for i in range(N)]
maxx = max([area(x) for x in itertools.combinations(point,3)])
print("%.3f"%maxx)