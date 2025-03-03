def f(st, fn):
    if st == fn: return 1
    if st < fn: return 0
    return f(st-2, fn) + f(st//2, fn)

print(f(38, 16)*f(16, 2))