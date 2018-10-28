# TurtleTest.py

from turtle import *
from tkinter import *
import turtle


# Create 2 pen objects
pen1 = Pen()
pen2 = Pen()

# Set the screen's background color
pen1.screen.bgcolor("#94B3C6")

# Set the pen colors
pen1.color('#5D5732')
pen2.color('#5D3237')

'''
# Move pens
pen1.forward(100)
pen2.backward(100)

# Move the pen without leaving a trail
pen1.up() #lift up the pen
pen1.goto(-100, 100)
pen1.down() #set the pen back down
'''

pen1.speed(10)
pen2.speed(10)

turn = True

for i in range(20):
    if turn:
        pen1.circle(5*i)
        pen1.circle(-5*i)
        pen1.left(i)

        if i % 5 == 0:
            turn = False
    if not turn:
        pen2.circle(5*i)
        pen2.circle(-5*i)
        pen2.right(i)

        if i % 5 == 0:
            turn = True

ts = turtle.getscreen()
ts.getcanvas().postscript(file="duck.eps")



