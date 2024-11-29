lst = [int(i) for i in open('text_7637.txt')]

max_sum_number = 0
count = 0
min_number = min(lst)

for i in range(len(lst) - 1):
    if lst[i] % 16 == min_number or lst[i+1] % 16 == min_number:
        max_sum_number = max(max_sum_number, lst[i] + lst[i+1])
        count += 1
print(count, max_sum_number)