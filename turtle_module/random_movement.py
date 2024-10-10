import turtle as t
import random

degrees = [90, 180, 0, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
my_turtle = t.Turtle() 
for _ in range(200):
    directions = [my_turtle.right, my_turtle.left]
    set_direction = random.choice(directions)
    set_direction(random.choice(degrees))
    my_turtle.color(random.choice(colours))
    my_turtle.pensize(5)
    my_turtle.speed(10)
    my_turtle.forward(30)