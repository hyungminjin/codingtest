# 연습문제 8번

import turtle
t = turtle.Turtle()
t.shape("turtle")

x = [0] * 3
y = [0] * 3

x[0] = int(input("x1: "))
y[0] = int(input("y1: "))
x[1] = int(input("x2: "))
y[1] = int(input("y2: "))
x[2] = int(input("x3: "))
y[2] = int(input("y3: "))

t.up()
t.goto(x[0],y[0])
t.down()
t.goto(x[1],y[1])
t.goto(x[2],y[2])
