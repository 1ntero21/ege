def f(st, fn):
    if st == fn: return 1
    if st < fn: return 0
    return f(st-2, fn) + f(st//2, fn) + f(st//3, fn)

print(f(50, 18) * f(18, 3))