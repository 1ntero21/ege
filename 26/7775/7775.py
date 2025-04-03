with open('text') as fin:
    N = int(fin.readline())
    points = list(map(int, fin.readline().split()))
    arr = [list(map(int, i.split())) for i in fin.readlines()]


participants = []
for i in arr:
    grade = sum(points[q]*i[q+1] for q in range(len(points)))
    fine = sum(points[q]*i[q+1] for q in range(len(points)) if (i[q+1] == -1))
    miss = i.count(0)
    participants.append([i[0], grade, fine, miss])

participants.sort(key=lambda x: (-x[1], -x[2], x[3], x[0]))

per_20 = int(N*0.2 - 1)
part_20 = participants[per_20]
top_part = participants[:per_20]

for i in participants[per_20:]:
    if all(part_20[q] == i[q] for q in range(1, 4)):
        top_part.append(i)
    else:
        break

no_top_part = []
for i in participants[len(top_part):]:
    if i[1] > 0:
        no_top_part.append(i)
    else:
        break

sum = sum(i[1] for i in no_top_part[:int(len(no_top_part)*0.1)])

print(no_top_part[0][0], sum)