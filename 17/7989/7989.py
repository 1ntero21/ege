def f(n):
    return sum(map(int, str(n)))


arr = [int(i) for i in open('text_7989')]
summ_num_13 = f([i for i in arr if i % 13 == 0][12])
summ_num_25 = f([i for i in arr if i % 25 == 0][24])
summ = 0
count = 0

for i in range(len(arr) - 2):
    if any(len(str(q)) == 3 for q in arr[i:i+3]):
        if sum([1 if f(q) == summ_num_13 else 0 for q in arr[i:i+3]]) <= 1:
            if sum([1 if f(q) == summ_num_25 else 0 for q in arr[i:i+3]]) >= 2:
                count += 1
                summ += sum(arr[i:i+3])
print(count, int(summ/count))