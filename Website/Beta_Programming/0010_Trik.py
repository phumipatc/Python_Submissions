order = input()
A,B,C = 1,0,0
for x in order:
	if(x == 'A'):
		A,B = B,A
	elif(x == 'B'):
		B,C = C,B
	else:
		A,C = C,A
if(A):
	print(1)
elif(B):
	print(2)
else:
	print(3)