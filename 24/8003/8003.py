def simple_num(n):
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i += 1
    return True


def f(lst):
    for i in lst:
        if len(i) == 5:
            i = int(i)
            if i ** 0.5 == int(i ** 0.5):
                if simple_num(i ** 0.5):
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