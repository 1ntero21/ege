from turtle import *

screensize(2500, 2500)
color('green')
tracer(0)
lt(90)
z = 30

# Повтори 3 [Вперёд 7 Направо 90 Вперёд 12 Направо 90]
# Поднять хвост
# Вперёд 4 Направо 90 Вперёд 6 Налево 90
# Опустить хвост
# Повтори 4 [Вперёд 83 Направо 90 Вперёд 77 Направо 90]

for _ in range(3):
    fd(7*z)
    rt(90)
    fd(12*z)
    rt(90)

up()
fd(4*z)
rt(90)
fd(6*z)
lt(90)

down()
for _ in range(4):
    fd(83*z)
    rt(90)
    fd(77*z)
    rt(90)

up()
for x in range(0, 13):
    for y in range(0, 8):
        goto(x*z, y*z)
        dot(5, 'red')

done()