namelist = ["winn","thanarak","somchai","ricky","tao","wanida","peerapol"]
def count_name(alp) :
	countt = 0
	for i in namelist :
		if alp in i :
			countt+=1
	return countt

target = input()
print(count_name(target))
