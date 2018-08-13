import snake as s
import random
import sys

choices = ['l', 'r', 'f']
score = 0

next_press = random.choice(choices)
score = s.forwards_ai(next_press)
while(score == None):
	#s.visualize_canvas_text()
	next_press = random.choice(choices)
	score = s.forwards_ai(next_press)
print(score)
