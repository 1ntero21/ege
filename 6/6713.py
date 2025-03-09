from turtle import *

screensize(2500, 2500)
tracer(0)
lt(90)
color('green')
z = 30


for _ in range(2):
    fd(13*z)
    rt(90)
    fd(20*z)
    rt(90)

up()
fd(8*z)
rt(90)
rt(180)
fd(3*z)
rt(180)
lt(90)

down()
for _ in range(2):
    fd(16*z)
    rt(90)
    fd(8*z)
    rt(90)

up()
for x in range(-3, 21):
    for y in range(0, 25):
        goto(x*z, y*z)
        dot(5, 'red')

done()