arr = [int(i) for i in open('text_7936')]
max_num = max([i for i in arr if (len(str(abs(i))) == 5 and str(i)[-2:] == '43')])
min_sum = max_num**2
count = 0


for i in range(len(arr) - 2):
    if any((len(str(abs(q))) == 5 and str(q)[-2:] == '43') for q in arr[i:i+3]):
        if sum(q**2 for q in arr[i:i+3]) <= max_num**2:
            count += 1
            min_sum = min(sum(q**2 for q in arr[i:i+3]), min_sum)

print(count, min_sum)
