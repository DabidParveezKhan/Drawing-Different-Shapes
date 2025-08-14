from turtle import Turtle,Screen
import random
colors=["forest green","deep sky blue","gold","orange","orange","pale violet red","turquoise",
        "green yellow","green yellow"]
tim=Turtle()
tim.shape("arrow")
tim.color("black")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
     tim.forward(100)
     tim.right(angle)

for shape_sides in range (3,11):
    tim.color(random.choice(colors))
    draw_shape(shape_sides)















screen=Screen()
screen.exitonclick()