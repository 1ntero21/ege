def f(claster):
    sum_min = 10**30
    x, y = 0, 0
    for x1, y1 in claster:
        sum = 0
        for x2, y2 in claster:
            sum += ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        if sum_min > sum:
            sum_min = sum
            x, y = x1, y1
    return x, y
with open('27_B_21425.txt') as fin:
    arr = [list(map(float, i.replace(',', '.').split())) for i in fin.readlines()]

claster_1 = []
claster_2 = []
claster_3 = []

for i in range(len(arr)):
    x, y = arr[i]
    if x < 0:
        claster_1.append(arr[i])
    elif y > 0:
        claster_2.append(arr[i])
    elif y < 0:
        claster_3.append(arr[i])


print(len(arr), len(claster_1), len(claster_2), len(claster_3))

x1, y1 = f(claster_1)
x2, y2 = f(claster_2)
x3, y3 = f(claster_3)
print((x1+x2+x3)/3*10_000, (y1+y2+y3)/3*10_000)

# 1)167990 73043
# 2)122627 29105