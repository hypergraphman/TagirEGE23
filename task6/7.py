from turtle import *


def move(a, b):
    global x, y
    x += a
    y += b
    goto(x * cell, y * cell)


speed(0.0001)
cell = 30
left(90)
x = y = 0

# задача
for i in range(15):
    move(10, 10)
    move(3, -6)
    move(-9, 3)

penup()
for x in range(15):
    for y in range(15):
        goto(x * cell, y * cell)
        dot(3, 'red')

done()
