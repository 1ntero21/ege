def f(st, fn):
    if st == fn: return 1
    if st< fn: return 0
    return f(st-1, fn) + f(st-2, fn) + f(st//3, fn)

print(f(16, 11) * f(11, 6))