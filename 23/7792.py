# В задании опечатка, должно быть не содержит.

def f(n, last):
    if n == last: return 1
    if n == 18: return 0
    if n <= last: return 0
    return f(n-2, last) + f(n//2 if n%2==0 else n-3, last)

print(f(55, 3))