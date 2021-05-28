n,m = [int(x) for x in input().split()]
a = [[0]*m]*n
b = [[0]*m]*n
for i in range(n):
	num = [int(x) for x in input().split()]
	a[i] = num[:]
for i in range(n):
	num = [int(x) for x in input().split()]
	b[i] = num[:]
for i in range(n):
	for j in range(m):
		print(a[i][j]+b[i][j],end=' ')
	print()