import turtle

import colorgram
# Extract colors from image by colorgram Module:
# colors = colorgram.extract('painting.jpg', 25)
# rgb_colors = []
# for x in range(25):
#     rgb_colors.append((colors[x].rgb.r, colors[x].rgb.g, colors[x].rgb.b))
from turtle import Turtle,Screen
from Drawer import Drawer
import random
turtle.colormode(255)
t = Turtle()
t.hideturtle()
t.speed(0)
t.penup()

drawer = Drawer(t)
drawer.draw_circle()

screen = Screen()
screen.exitonclick()
