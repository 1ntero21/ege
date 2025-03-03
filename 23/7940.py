def f(st, fn):
    if st == 24: return 0
    if st == fn: return 1
    if st <= fn: return 0
    return f(st-1, fn) + f(st-6, fn) + f(st//2, fn)

print(f(34, 29)*f(29, 19)*f(19, 6))