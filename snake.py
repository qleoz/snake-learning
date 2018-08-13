import random
import threading, time
from tkinter import *

#frame speed in ms
SPEED = 500

def visualize_canvas(board, snake):
    if(board == None):
        return False
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if(board[i][j] == 1):
                canvas.create_rectangle(i*50, j*50, i*50+50, j*50+50, fill="green")
            elif(board[i][j] == 2):
                canvas.create_rectangle(i*50, j*50, i*50+50, j*50+50, fill="yellow")
            else:
                canvas.create_rectangle(i*50, j*50, i*50+50, j*50+50, fill="gray")
    canvas.create_rectangle(snake[0][0]*50, snake[0][1]*50, snake[0][0]*50+50, snake[0][1]*50+50, fill="red")
    return True

def visualize_canvas_nogui(board, snake):
    if(board == None):
        return False
    return True

def visualize_canvas_text():
    print()
    for i in board:
        print(i)

#resets game values, returns a board and snake 2d array
def reset():
    global board
    global snake
    global direction
    global score_alive
    global score_eat
    board = [[0 for i in range(10)] for j in range(10)]
    snake = [[5, 5]]
    board = update(board, snake)
    board = addfood(board, snake)
    direction = 'l'
    score_alive = 0
    score_eat = 0

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
    global score_eat
    global score_alive
    temp = checknext(board, snake, direction)
    if(temp == None):
        return None
    if(board[temp[0]][temp[1]] == 2):
        score_eat+=10
        return eatmove(board, snake, temp)
    else:
        score_alive+=1
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

#changes direction into next_input, resets next_input to None
def change_direction():
    global direction
    global next_input
    if(next_input == 'l'):
        if(direction == 'u'):
            direction = 'r'
        elif(direction == 'l'):
            direction = 'u'
        elif(direction == 'd'):
            direction = 'l'
        else:
            direction = 'd'
    if(next_input == 'r'):
        if(direction == 'u'):
            direction = 'l'
        elif(direction == 'r'):
            direction = 'u'
        elif(direction == 'd'):
            direction = 'r'
        else:
            direction = 'd'    
    next_input = None

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

def create_grid(event=None):
    w = canvas.winfo_width() # Get current width of canvas
    h = canvas.winfo_height() # Get current height of canvas
    canvas.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 50
    for i in range(0, w, 50):
        canvas.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 50
    for i in range(0, h, 50):
        canvas.create_line([(0, i), (w, i)], tag='grid_line')

def left(event=None):
    global next_input
    next_input = 'l'    

def right(event=None):
    global next_input
    next_input = 'r'    

def forwards():
    global board
    global snake
    global direction
    change_direction()
    board = step(board, snake, direction)
    score.set("Score: " + str(score_alive + score_eat))
    cont = visualize_canvas(board, snake)
    if(cont):
        root.after(SPEED, forwards)
    else:
        print("GAME OVER")
        print("Max length: ", len(snake))
        print("Score: ", score_eat + score_alive)
        root.destroy()

def run():
    root.after(SPEED, forwards)
    root.mainloop()
    return score_alive+score_eat

def forwards_ai(keypress):
    global board
    global snake
    global direction
    global next_input
    next_input = keypress
    change_direction()
    board = step(board, snake, direction)
    score.set("Score: " + str(score_alive + score_eat))
    cont = visualize_canvas_nogui(board, snake)
    if(not cont):
        root.destroy()
        return score_alive+score_eat
    else:
        return None

board = []
snake = []
direction = None
next_input = None
score_alive = 0
score_eat = 0

reset()

root = Tk()
root.bind('a', left)
root.bind('d', right)
root.bind('<Left>', left)
root.bind('<Right>', right)

rootFrame = Frame(root, width=500, height=50, bg="white")
rootFrame.pack()

score = StringVar()
score.set("Score: " + str(score_alive + score_eat))
scoreLabel = Label(rootFrame, textvariable=score).pack()

canvas = Canvas(root, width=500, height=500, bg="gray")
canvas.bind('<Configure>', create_grid)
canvas.pack()

visualize_canvas(board, snake)
