def to_three(n):
    res = ''
    while n:
        res += str(n%3)
        n //= 3
    return res[::-1]

def f(n):
    if n % 3 == 0:
        return int(to_three(n) + to_three(n)[-2:], 3)
    return int(to_three(n) + to_three(sum(map(int, str(n)))), 3)


arr = []
for N in range(1, 1000):
    if f(N) > 220 and f(N) % 2 == 0:
        arr.append(f(N))
print(min(arr))