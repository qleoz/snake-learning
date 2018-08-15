import snake as s
import random
import sys
import math as m

choices = ['l', 'r', 'f']
board = []
snake = []
direction = ''

def generate_next_move():
    return random.choice(choices)

def get_info(b, s, d):
    global board, snake, direction
    board = b
    snake = s
    direction = d
