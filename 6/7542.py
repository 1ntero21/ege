from turtle import *

color('green')
tracer(0)
lt(90)
z = 30


for _ in range(2):
    fd(6*z)
    rt(90)
    fd(12*z)
    rt(90)

up()
fd(1*z)
rt(90)
fd(3*z)
lt(90)

down()
for _ in range(2):
    fd(77*z)
    rt(90)
    fd(45*z)
    rt(90)

up()
for x in range(0, 15):
    for y in range(0, 7):
        goto(x*z, y*z)
        dot(5, 'red')

done()