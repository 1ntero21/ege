def f(n):
    return sum(map(int, str(n)))


arr = [int(i) for i in open('text_7988')]
count_num_531 = len([i for i in arr if i % 531 == 0])
count_num_773 = len([i for i in arr if i % 773 == 0])
summ = 0
count = 0

for i in range(len(arr) - 2):
    if any(len(str(q)) == 3 for q in arr[i:i+3]):
        if sum([1 if f(q) == count_num_531 else 0 for q in arr[i:i+3]]) <= 1:
            if sum([1 if f(q) == count_num_773 else 0 for q in arr[i:i+3]]) >= 2:
                count += 1
                summ += sum(arr[i:i+3])
print(count, int(summ/count))