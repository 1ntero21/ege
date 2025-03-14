def f(lst):
    for i in lst:
        if len(i) == 10:
            sum_num = sum(map(int, i))
            if sum_num ** 0.5 == int(sum_num ** 0.5):
                return True
    return False


with open('text') as fin:
    s = fin.readline().strip()

max_len = 0
subs = ''

for i in range(len(s)):
    digit = s[i]
    if digit.isdigit():
        subs = digit
        while subs:
            i += 1
            if i >= len(s):
                break
            if s[i].isdigit():
                subs += s[i]
            else:
                if subs[-1].isdigit():
                    subs += s[i]
                else:
                    subs = subs[:-1]
                    if f(subs.split('=')):
                        max_len = max(max_len, len(subs))
                    subs = ''

print(max_len)