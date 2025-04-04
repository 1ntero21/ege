with open('text') as fin:
    N = int(fin.readline())
    arr = [list(map(int, i.split())) for i in fin.readlines()]

arr.sort(key=lambda x: (x[0], x[1], x[2]))

aver = sum(i[1] for i in arr) / len(arr)
expensive = [i for i in arr if i[1] > aver]

leaders = []

id = expensive[0][0]
count_zero = 0
count_one = 0

for i in range(1, len(expensive)):
    if expensive[i][0] == id:
        if expensive[i][-1]:
            count_one += 1
        else:
            count_zero += 1

    else:
        leaders.append([id, count_one, count_zero, expensive[i-1][1]])
        id = expensive[i][0]
        if expensive[i][-1]:
            count_one = 1
            count_zero = 0
        else:
            count_zero = 1
            count_one = 0

leaders.sort(key=lambda x: (-x[2], -x[-1]))

print(leaders[0][1]*leaders[0][-1], leaders[0][0])