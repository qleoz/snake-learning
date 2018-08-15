import random
import threading, time
from tkinter import *
import snake
import ai

class snake_gui:
    
    def __init__(self, frametime, playmode):
        #how long each frame is
        self.SPEED = frametime

        #game mode 1=human 2=ai
        self.mode = playmode
        self.s = snake.snake()
        self.root = Tk()

        self.rootFrame = Frame(self.root, width=500, height=50, bg="white")
        self.rootFrame.pack()

        self.score = StringVar()
        self.score.set("Score: " + str(self.s.get_score_alive() + self.s.get_score_eat()))
        self.scoreLabel = Label(self.rootFrame, textvariable=self.score).pack()
        self.canvas = Canvas(self.root, width=500, height=500, bg="gray")
        self.canvas.pack()

        self.root.bind('a', self.left)
        self.root.bind('d', self.right)
        self.root.bind('<Left>', self.left)
        self.root.bind('<Right>', self.right)
        self.canvas.bind('<Configure>', self.create_grid)        

    def visualize_canvas(self):
        if(self.s.get_board() == None):
            return False
        for i in range(10):
            for j in range(10):
                if(self.s.get_board()[i][j] == 1): #snake body
                    self.canvas.create_rectangle(j*50, i*50, j*50+50, i*50+50, fill="green")
                elif(self.s.get_board()[i][j] == 2): #food pellet
                    self.canvas.create_rectangle(j*50, i*50, j*50+50, i*50+50, fill="yellow")
                else: #board background
                    self.canvas.create_rectangle(j*50, i*50, j*50+50, i*50+50, fill="gray")
        self.canvas.create_rectangle(self.s.get_snake()[0][1]*50, self.s.get_snake()[0][0]*50, self.s.get_snake()[0][1]*50+50, self.s.get_snake()[0][0]*50+50, fill="red") #snakehead
        return True

    def visualize_canvas_nogui():
        if(s.get_board() == None):
            return False
        return True

    def create_grid(self, event=None):
        w = self.canvas.winfo_width() # Get current width of canvas
        h = self.canvas.winfo_height() # Get current height of canvas
        self.canvas.delete('grid_line') # Will only remove the grid_line

        # Creates all vertical lines at intevals of 50
        for i in range(0, w, 50):
            self.canvas.create_line([(i, 0), (i, h)], tag='grid_line')

        # Creates all horizontal lines at intevals of 50
        for i in range(0, h, 50):
            self.canvas.create_line([(0, i), (w, i)], tag='grid_line')

    def left(self, event=None):
        self.s.set_next_input('l')  

    def right(self, event=None):
        self.s.set_next_input('r')

    #advances one "action" in game of snake, repeats as long as not game over
    def forwards(self):
        self.s.change_direction()
        self.s.set_board(self.s.step())
        self.score.set("Score: " + str(self.s.get_score_alive() + self.s.get_score_eat()))
        cont = self.visualize_canvas()
        if(cont):
            self.root.after(self.SPEED, self.forwards)
        else:
            print("GAME OVER")
            print("Max length: ", len(self.s.get_snake()))
            print("Score: ", self.s.get_score_eat() + self.s.get_score_alive())
            self.root.destroy()

    #starts a game of snake
    def run(self):
        self.s.reset()
        if (self.mode == 1):
            self.root.after(self.SPEED, self.forwards)
        else:
            self.root.after(self.SPEED, self.forwards_ai)
        self.root.mainloop()
        return self.s.get_score_alive() + self.s.get_score_eat()

    def forwards_ai(self):
        self.get_next_move()
        self.s.change_direction()
        self.s.set_board(self.s.step())
        self.score.set("Score: " + str(self.s.get_score_alive() + self.s.get_score_eat()))
        cont = self.visualize_canvas()
        if(cont):
            self.root.after(self.SPEED, self.forwards_ai)
        else:
            print("GAME OVER")
            print("Max length: ", len(self.s.get_snake()))
            print("Score: ", self.s.get_score_eat() + self.s.get_score_alive())
            self.root.destroy()

    def get_next_move(self):
        temp = ai.generate_next_move()
        if(temp == 'l'):
            self.left()
        if(temp == 'r'):
            self.right()