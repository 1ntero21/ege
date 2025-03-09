from turtle import *

tracer(0)
color('green')
screensize(2500, 2500)
lt(90)
z = 30


for _ in range(9):
    fd(22*z)
    rt(90)
    fd(6*z)
    rt(90)

up()
fd(1*z)
rt(90)
fd(5*z)
lt(90)

down()
for _ in range(9):
    fd(53*z)
    rt(90)
    fd(75*z)
    rt(90)

up()
for x in range(0, 2):
    for y in range(0, 22):
        goto(x*z, y*z)
        dot(5, 'red')

done()