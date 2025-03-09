from turtle import *

color('green')
tracer(0)
lt(90)
z = 30
screensize(2500, 2500)

for _ in range(8):
    fd(16*z)
    rt(90)
    fd(22*z)
    rt(90)

up()
fd(5*z)
rt(90)
fd(5*z)
lt(90)

down()
for _ in range(8):
    fd(52*z)
    rt(90)
    fd(77*z)
    rt(90)

up()
for x in range(5, 25):
    for y in range(3, 25):
        goto(x*z, y*z)
        dot(5, 'red')

done()