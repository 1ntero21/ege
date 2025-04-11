def f(claster):
    sum_max = 0
    x, y = 0, 0
    for x1, y1 in claster:
        sum = 0
        for x2, y2 in claster:
            sum += ((x2-x1)**2 + (y2-y1)**2)**0.5
        if sum_max < sum:
            sum_max = sum
            x, y, = x1, y1
    return x, y

with open('27.19.B_20497.txt') as fin:
    arr = [list(map(float, i.replace(',', '.').split())) for i in fin.readlines()]

claster_1 = []
claster_2 = []
claster_3 = []
claster_4 = []
claster_5 = []

for i in range(len(arr)):
    x, y = arr[i]
    if x < -35 and -40 < y < 40:
        claster_1.append(arr[i])
    elif -40 < x < -21 and 40 < y < 120:
        claster_2.append(arr[i])
    elif -30 < x < -10 and y < 40:
        claster_3.append(arr[i])
    elif -15 < x < 10 and y > 40:
        claster_4.append(arr[i])
    elif x > 0 and y < 40:
        claster_5.append(arr[i])


T_x = (f(claster_1)[0] + f(claster_2)[0] + f(claster_3)[0] + f(claster_4)[0] + f(claster_5)[0])/5
T_y = (f(claster_1)[1] + f(claster_2)[1] + f(claster_3)[1] + f(claster_4)[1] + f(claster_5)[1])/5

print(T_x*10_000, T_y*10_000)

# 1) 13258 2656
# 2) -209434 474989