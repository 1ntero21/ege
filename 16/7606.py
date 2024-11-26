from sys import setrecursionlimit

setrecursionlimit(2500)

def f(n):
    if n <= 2025: return 1
    return f((n + 2024) // 2025) + 1

print(f(sum(i**i for i in range(1, 2026))))