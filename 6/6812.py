from turtle import *

screensize(2500, 2500)
tracer(0)
color('green')
lt(90)
z = 30


rt(90)
for _ in range(3):
    rt(45)
    fd(10*z)
    rt(45)

rt(315)
fd(10*z)

for _ in range(2):
    rt(90)
    fd(10*z)

up()
for x in range(-15, 10):
    for y in range(-15, 10):
        goto(x*z, y*z)
        dot(5, 'red')

done()