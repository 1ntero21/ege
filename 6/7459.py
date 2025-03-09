from turtle import *

color('green')
tracer(0)
screensize(2500, 2500)
lt(90)
z = 30


for _ in range(4):
    fd(28*z)
    rt(90)
    fd(26*z)
    rt(90)

up()
fd(8*z)
rt(90)
fd(7*z)
lt(90)

down()
for _ in range(4):
    fd(67*z)
    rt(90)
    fd(98*z)
    rt(90)

up()
for x in range(7, 27):
    for y in range(8, 29):
        goto(x*z, y*z)
        dot(5, 'red')

done()