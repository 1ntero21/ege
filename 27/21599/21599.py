def f(claster):
    x, y = 0, 0
    sum_min = 10**10
    for x1, y1 in claster:
        sum = 0
        for x2, y2 in claster:
            sum += ((x2-x1)**2 + (y2-y1)**2)**0.5
        if sum <= sum_min:
            x, y = x1, y1
            sum_min = sum
    return x, y


with open('27_B_21599.txt') as fin:
    arr = [list(map(float, i.replace(',', '.').split())) for i in fin.readlines()]

claster = [[], [], [], [], [], []]

for i in arr:
    x, y = i
    if y < -5:
        claster[0].append(i)
    elif y < (1/2)*x:
        claster[1].append(i)
    elif y < (3/2)*x + 10:
        claster[2].append(i)
    elif x > -10:
        claster[3].append(i)
    elif y > -2*x - 25:
        claster[4].append(i)
    else:
        claster[5].append(i)


print(len(arr), len(claster[0]), len(claster[1]), len(claster[2]), len(claster[3]), len(claster[4]), len(claster[5]))


T_x = sum(f(i)[0] for i in claster) / 6
T_y = sum(f(i)[1] for i in claster) / 6

print(T_x*10_000, T_y*10_000)

# 1) 178755 2896
# 2) 37392 50998