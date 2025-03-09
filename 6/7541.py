from turtle import *

tracer(0)
color('green')
screensize(2500, 2500)
lt(90)
z = 30


for _ in range(10):
    fd(22*z)
    rt(90)
    fd(16*z)
    rt(90)

up()
fd(1*z)
rt(90)
fd(1*z)
lt(90)

down()
for _ in range(10):
    fd(72*z)
    rt(90)
    fd(79*z)
    rt(90)

up()
for x in range(1, 17):
    for y in range(1, 23):
        goto(x*z, y*z)
        dot(5, 'red')

done()