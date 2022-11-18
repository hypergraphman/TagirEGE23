from turtle import *

speed(0.0001)
cell = 10
left(90)
pendown()

# задача
for i in range(11):
    forward(36 * cell)
    right(72)
stamp()
penup()
for x in range(2):
    for y in range(37):
        goto(x * cell, y * cell)
        dot(3, 'red')
goto(0, 0)
done()
