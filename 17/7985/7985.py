def f1(n):
    if str(n)[-1] == str(max_abs_num)[-1]:
        return 1
    return 0

def f2(n):
    if str(n)[-1] == str(max_num)[-1]:
        return 1
    return 0


arr = [int(i) for i in open('text_7985')]
max_abs_num = max(abs(i) for i in arr)
max_num = max(arr)
summ = 0
count = 0

for i in range(len(arr) - 2):
    if any(len(str(abs(q))) == 4 for q in arr[i:i+3]):
        if sum([f1(q) for q in arr[i:i+3]]) <= 1:
            if sum([f2(q) for q in arr[i:i+3]]) >= 1:
                count += 1
                summ += sum(arr[i:i+3])
print(count, int(summ/count))
