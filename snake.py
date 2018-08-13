import random

def visualize(board):
	print()
	if(board == None):
		print("RIP RIP RIP RIP")
		return None
	for l in board:
		print(l)

#resets game values, returns a board and snake 2d array
def reset():
	board = [[0 for i in range(10)] for j in range(10)]
	snake = [[5, 5]]
	board = update(board, snake)
	board = addfood(board, snake)
	return board, snake

#updates board with snake position
def update(board, snake):
	for s in snake:
		board[s[0]][s[1]] = 1
	return board

#spawns a new food dot on board
def addfood(board, snake):
	empty = []
	for i in range(0, 9):
		for j in range(0, 9):
			if(board[i][j] == 0):
				empty.append([i, j])
	if(len(empty) == 0):
		print("WIN WIN WIN WIN WIN")
		return board
	select = random.randint(0, len(empty))
	board[empty[select][0]][empty[select][1]] = 2
	return board

#returns board after snake has moved, eaten, or game over
def step(board, snake, direction):
	temp = checknext(board, snake, direction)
	if(temp == None):
		return None
	if(board[temp[0]][temp[1]] == 2):
		return eatmove(board, snake, temp)
	else:
		return move(board, snake, temp)

#makes and returns a coordinate if next move is valid (empty square, food)
#returns null if bad move (borders, snake)
def checknext(board, snake, direction):
	temp = []
	if(direction == 'u'):
		temp = [snake[0][0] - 1, snake[0][1]]
	elif(direction == 'd'):
		temp = [snake[0][0] + 1, snake[0][1]]
	elif(direction == 'l'):
		temp = [snake[0][0], snake[0][1] - 1]
	else:
		temp = [snake[0][0], snake[0][1] + 1]
	#check out of bounds
	for t in temp:
		if(t < 0 or t > 9):
			return None
	#check if hits self
	if(temp in snake):
		return None

	return temp

#grows snake by 1, makes new food, returns new board
def eatmove(board, snake, loc):
	snake.insert(0, loc)
	board[loc[0]][loc[1]] = 1
	board = addfood(board, snake)
	return board

#moves snake by one, returns new board
def move(board, snake, loc):
	snake.insert(0, loc)
	tail = snake.pop()
	board[loc[0]][loc[1]] = 1
	board[tail[0]][tail[1]] = 0
	return board

def input_direction():
	d = input("u/d/l/r: ")
	return d

board = []
snake = []
direction = 'u'

board, snake = reset()
visualize(board)
while(board != None):
	direction = input_direction()
	board = step(board, snake, direction)
	visualize(board)
