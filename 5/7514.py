def f(n):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        return int('10' + bin_n, 2)
    return int('1' + bin_n + '01', 2)

arr = []
for N in range(1, 13):
    arr.append(f(N))
print(max(arr))
