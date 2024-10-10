
import turtle
import random
def random_color():
    r = random.random() 
    g = random.random()  
    b = random.random()  
    return (r, g, b)
canvas = turtle.Turtle()


for i in range(3,10):
  canvas.pencolor(random_color()) 
  angle=360/i
  for j in range(i):
    canvas.forward(100)
   
    canvas.right(angle)


turtle.done()


