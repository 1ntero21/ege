def f(st, fn):
    if st == fn: return 1
    if st < fn: return 0
    return f(st-2, fn) + f(st//2, fn)

print(f(32, 8) * f(8, 1))