n = int(input())
mn = 3000000000
mx = -3000000000
for i in range(n):
	num = int(input())
	mn = min(mn,num)
	mx = max(mx,num)
print(mn)
print(mx)