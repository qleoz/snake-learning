import snake as s
import random
import sys
import math as m

choices = ['l', 'r', 'f']
score = 0
best_score = 0

iterations = 50

def findfood(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 2):
                return [i, j]
    return None

#return True if nothing in front
def checkfront(board, snake, direction):
    return s.checknext(board, snake, direction)

#return True if nothing on left
def checkleft(board, snake, direction):
    if(direction == 'u'):
        tempdir = 'l'
    elif(direction == 'd'):
        tempdir = 'r'
    elif(direction == 'l'):
        tempdir = 'd'
    else:
        tempdir = 'u'
    return s.checknext(board, snake, tempdir)

#return True if nothing on right
def checkright(board, snake, direction):
    if(direction == 'u'):
        tempdir = 'r'
    elif(direction == 'd'):
        tempdir = 'l'
    elif(direction == 'l'):
        tempdir = 'u'
    else:
        tempdir = 'd'
    return s.checknext(board, snake, tempdir)

def food_dir(board, snake, direction):
    food = findfood(board)
    dx = food[1] - snake[0][1]
    dy = snake[0][0] - food[0]
    print("dx: ", dx, " dy: ", dy)
    angle = m.atan2(dy, dx)
    print('angle: ', angle)
    if(direction == 'l'):
        if(angle < 0):
            return 'l'
        if(angle > 0):
            return 'r'
    if(direction == 'u'):
        if(angle > m.pi/2 or angle < -m.pi/2):
            return 'l'
        if(angle < m.pi/2 and angle > -m.pi/2):
            return 'r'
    if(direction == 'r'):
        if(angle > 0):
            return 'l'
        if(angle < 0):
            return 'r'
    if(direction == 'd'):
        if(angle < m.pi/2 and angle > -m.pi/2):
            return 'l'
        if(angle > m.pi/2 or angle < -m.pi/2):
            return 'r'
    return 's'

def generate_next_move():
    return random.choice(choices)
