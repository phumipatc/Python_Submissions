# num = [int(x) for x in input().split()];
# num.sort();
# order = input();
# for x in order:
# 	print(num[ord(x)-ord('A')],end=' ');

num = [int(x) for x in input().split()];
num.sort();
order = input();
for x in order:
	if(x == 'A'):
		print(num[0],end=' ');
	elif(x == 'B'):
		print(num[1],end=' ');
	else:
		print(num[2],end=' ');