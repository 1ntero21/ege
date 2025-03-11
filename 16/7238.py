def f(n):
    if n >= 5000: return n
    if n % 5 != 0:
        return n*f(n+1)
    return n*f(n+2) / 5

print(f(4975) / f(4978))