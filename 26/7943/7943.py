with open('text') as fin:
    N = int(fin.readline())
    arr = [list(map(int, i.split())) for i in fin.readlines()]

arr.sort(key=lambda x: x[0])

list_task = []
id = ''
max_count = 0

for i in range(1, len(arr) - 1):
    if arr[i][0] == arr[i+1][0] or arr[i-1][0] == arr[i][0]:
        list_task.append(arr[i][1])

    else:
        list_task.sort()
        list_count = [0]*len(list_task)

        if list_task != []:
            for q in range(1, len(list_task)):
                if list_task[q] - list_task[q-1] == 1:
                    list_count[q] = list_count[q-1]+1

            if max_count < max(list_count) + 1:
                max_count = max(list_count) + 1
                id = arr[i-1][0]

        list_task = []

print(id, max_count)