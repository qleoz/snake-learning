import snake as s
import random
import sys

choices = ['l', 'r', 'f']
score = 0
best_score = 0

#iterations = input("How many runs? ")
iterations = 2000

next_press = random.choice(choices)
score = s.forwards_ai(next_press)
for i in range(int(iterations)):
	while(score == 0):
		#s.visualize_canvas_text()
		next_press = random.choice(choices)
		score = s.forwards_ai(next_press)
	print(score)
	if(score > best_score):
		best_score = score
	score = 0
	s.reset()
	# if(score >= best_score):
	# 	print(score)
	# 	best_score = score
	# 	score = 0
	# 	s.reset()
print("best: ", best_score)