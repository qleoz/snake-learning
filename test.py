import snake
import snake_gui

best = 0

for i in range(10):
    sgui = snake_gui.snake_gui(20,2)
    score = sgui.run()
    if(score > best):
        best = score
print("best score: ", best)
