def f(n):
    if n >= 1300: return n
    if n % 2 != 0:
        return n*f(n+1)
    return n*f(n+2) / 4

print(f(1286) / f(1290))