with open('text') as fin:
    N = int(fin.readline())
    arr = [[list(map(int, i.split()))[0], sum(map(int, i.split()[1:]))/4, list(map(int, i.split()))[1:].count(2)] for i in fin.readlines()]

arr.sort(key=lambda x: (x[2], -x[1], x[0]))

task_1 = arr[int(N*0.25) - 1][0]

new_arr = [i for i in arr if i[-1] > 0]
new_arr.sort(key=lambda x: (x[2], x[0]))
for i in new_arr:
    if i[-1] > 2:
        task_2 = i[0]
        break

print(task_1, task_2)