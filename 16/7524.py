from sys import setrecursionlimit
setrecursionlimit(2500)

def f(n):
    if n == 1:
        return 1
    return 2*n*f(n-1)

number = (f(2024)//16 - f(2023)) // f(2022)
print(number)
