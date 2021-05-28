import numpy as np
import copy as cp

pos = [(0,0)]
goal_state = [[1,2,3],[4,5,6],[7,8,0]]
for i in range(3):
	for j in range(3):
		pos.append((i,j))

def hcost(current_state):
	sum = 0
	for i in range(3):
		for j in range(3):
			now = current_state[i][j]
			# print(now)
			if now != 0:
				sum+= np.abs(i-pos[now][0]) + np.abs(j-pos[now][1])
				# print(i-pos[now][0],j-pos[now][1])
	return sum

def printf(current_state):
	for i in range(3):
		print(current_state[i][0],current_state[i][1],current_state[i][2])
	if current_state != goal_state:
		print("  |")
		print("  V")

def find(current_state,value):
	for i in range(3):
		for j in range(3):
			if current_state[i][j] == value:
				return i,j

def swap(initial_state):
	i,j = find(initial_state,0)
	possible_move = []
	# print(initial_state)
	if i-1 >= 0:
		current_state = cp.deepcopy(initial_state)
		current_state[i][j],current_state[i-1][j] = current_state[i-1][j],current_state[i][j]
		# print(current_state)
		possible_move.append(current_state)
	# print(initial_state)
	if i+1 < 3:
		current_state = cp.deepcopy(initial_state)
		current_state[i][j],current_state[i+1][j] = current_state[i+1][j],current_state[i][j]
		# print(current_state)
		possible_move.append(current_state)
	if j-1 >= 0:
		current_state = cp.deepcopy(initial_state)
		current_state[i][j],current_state[i][j-1] = current_state[i][j-1],current_state[i][j]
		# print(current_state)
		possible_move.append(current_state)
	if j+1 < 3:
		current_state = cp.deepcopy(initial_state)
		current_state[i][j],current_state[i][j+1] = current_state[i][j+1],current_state[i][j]
		# print(current_state)
		possible_move.append(current_state)
	return possible_move

def gcost(current_state):
	sum = 0
	for i in range(3):
		for j in range(3):
			if current_state[i][j] != goal_state[i][j]:
				sum+=1
	return sum

def solve(current_state):
	while current_state != goal_state:
		printf(current_state)
		possible_move = swap(current_state)
		minn = 1e9
		nextt = []
		for now in possible_move:
			sum = gcost(now) + hcost(now)
			# print(minn,sum)
			if minn > sum:
				minn = sum
				nextt = cp.deepcopy(now)
		current_state = cp.deepcopy(nextt)
		# current_state = cp.deepcopy(goal_state)
	printf(goal_state)

# solve([[5,2,4],[6,0,7],[1,8,3]])
solve([[2,3,6],[1,4,0],[7,5,8]])