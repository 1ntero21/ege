def f1(number):
    if str(number)[-1] == '7' and len(str(number)) == 4:
        return 1
    return 0

def f2(lst):
    num = 0
    for i in lst:
        if f1(i):
            num = max(num, i)
    return num


lst = [int(i) for i in open('text_7564.txt')]

max_num = f2(lst)
max_sum = 0
count = 0

for i in range(len(lst) - 1):
    new_lst = lst[i:i+3]
    if len(new_lst) == 3:
        if sum(f1(abs(q)) for q in new_lst) > 1:
            if sum(new_lst) > max_num:
                count += 1
                max_sum = max(max_num, sum(new_lst))
                print(new_lst)

print(count, max_sum)