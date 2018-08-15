import random
import threading, time
from tkinter import *

class snake:

    def __init__(self):
        self.board = []
        self.snake = []
        self.food = []
        self.direction = 'u'
        self.next_input = None
        self.score_alive = 0
        self.score_eat = 0

    def visualize_canvas_text(self):
        print()
        for i in self.board:
            print(i)

    #resets game values, returns a board and snake 2d array
    def reset(self):
        self.board = [[0 for i in range(10)] for j in range(10)]
        self.snake = [[5, 5]]
        self.board = self.update(self.board, self.snake)
        self.board = self.addfood(self.board, self.snake)
        self.direction = 'u'
        self.score_alive = 0
        self.score_eat = 0
        self.next_input = None

    #returns a board with updated values of snake position
    def update(self, board, snake):
        for s in snake:
            board[s[0]][s[1]] = 1
        return board

    #returns a board with new food pellet
    def addfood(self, board, snake):
        empty = []
        for i in range(10):
            for j in range(10):
                if(board[i][j] == 0):
                    empty.append([i, j])
        if(len(empty) == 0):
            print("WIN WIN WIN WIN WIN")
            return board
        select = random.choice(empty)
        food = select
        board[select[0]][select[1]] = 2
        return board

    #returns the resulting board after a) snake has moved b) eaten or c) game over
    def step(self):
        temp = self.checknext()
        if(temp == None): #gameover
            return None
        if(self.board[temp[0]][temp[1]] == 2): #ate pellet
            self.score_eat+=10
            return self.eatmove(self.board, self.snake, temp)
        else: #moved a square in direction
            self.score_alive+=1
            return self.move(self.board, self.snake, temp)

    #returns a coordinate [a,b] if future move in direction is valid (empty square, food)
    #returns null if bad move (borders, snake)
    def checknext(self):
        temp = []
        if(self.direction == 'u'):
            temp = [self.snake[0][0] - 1, self.snake[0][1]]
        elif(self.direction == 'd'):
            temp = [self.snake[0][0] + 1, self.snake[0][1]]
        elif(self.direction == 'l'):
            temp = [self.snake[0][0], self.snake[0][1] - 1]
        else:
            temp = [self.snake[0][0], self.snake[0][1] + 1]
        #check out of bounds
        for t in temp:
            if(t < 0 or t > 9):
                return None
        #check if hits self
        if(temp in self.snake):
            return None

        return temp

    #changes direction into next_input, resets next_input to None
    def change_direction(self):
        if(self.next_input == 'l'):
            if(self.direction == 'u'):
                self.direction = 'l'
            elif(self.direction == 'l'):
                self.direction = 'd'
            elif(self.direction == 'd'):
                self.direction = 'r'
            else:
                self.direction = 'u'
        if(self.next_input == 'r'):
            if(self.direction == 'u'):
                self.direction = 'r'
            elif(self.direction == 'r'):
                self.direction = 'd'
            elif(self.direction == 'd'):
                self.direction = 'l'
            else:
                self.direction = 'u'    
        self.next_input = None

    #returns updated board with snake grown by 1 and makes new food pellet
    def eatmove(self, board, snake, loc):
        snake.insert(0, loc)
        board[loc[0]][loc[1]] = 1
        board = self.addfood(board, snake)
        return board

    #returns updated board with snake moved forward by 1
    def move(self, board, snake, loc):
        snake.insert(0, loc)
        tail = snake.pop()
        board[loc[0]][loc[1]] = 1
        board[tail[0]][tail[1]] = 0
        return board

    def set_next_input(self, direction):
        self.next_input = direction
    def set_board(self, b):
        self.board = b

    def get_board(self):
        return self.board
    def get_snake(self):
        return self.snake
    def get_food(self):
        return self.food
    def get_direction(self):
        return self.direction
    def get_next_input(self):
        return self.next_input
    def get_score_alive(self):
        return self.score_alive
    def get_score_eat(self):
        return self.score_eat
