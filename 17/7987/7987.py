def f1(n):
    if n % 5 == min_num % 7:
        return 1
    return 0

def f2(n):
    if n % 7 == max_num % 5:
        return 1
    return 0


arr = [int(i) for i in open('text_7987')]
max_num = max(arr)
min_num = min(arr)
summ = 0
count = 0

for i in range(len(arr) - 2):
    if any(len(str(q)) == 3 for q in arr[i:i+3]):
        if sum([f1(q) for q in arr[i:i+3]]) <= 1:
            if sum([f2(q) for q in arr[i:i+3]]) >= 2:
                count += 1
                summ += sum(arr[i:i+3])
print(count, int(summ/count))