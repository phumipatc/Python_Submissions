import numpy as np
def bubble_sort(numlist) :
	n = len(numlist)
	for i in range(n) :
		for j in range(n-1) :
			if numlist[j] > numlist[j+1] :
				numlist[j],numlist[j+1] = numlist[j+1],numlist[j]
	return numlist
# ค่า max อยู่ที่ numlist[n-1]
query = np.random.randint(1,1e3,10)
ans = bubble_sort(query)
n = len(ans)
print(ans[n-1])