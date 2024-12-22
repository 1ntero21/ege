def f(n):
    if n == 1: return 1
    if n == 28: return 0
    if n <= 1: return 0
    return f(n-2) + f(n//2 if n%2==0 else n-3)

print(f(98))