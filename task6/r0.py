from turtle import *

speed(0.0001)
cell = 30
left(90)
pendown()

# задача
for i in range(7):
    forward(10 * cell)
    right(120)

penup()
for x in range(15):
    for y in range(15):
        goto(x * cell, y * cell)
        dot(3, 'red')

done()
