def deli(n):
    i = 1
    arr = []
    while i <= n**0.5:
        if n % i == 0:
            arr.append(i)
            arr.append(n//i)
        i += 1
    return sum(set(arr))

def f(st, fn):
    if st == fn: return 1
    if st > fn: return 0
    return f(st+1, fn) + f(deli(st), fn)

print(f(2, 24))