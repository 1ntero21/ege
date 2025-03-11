def f(n):
    if n >= 1900: return n
    if n % 3 != 0:
        return n*f(n+1)
    return n*f(n+2) / 3

print(f(1875) / f(1880))