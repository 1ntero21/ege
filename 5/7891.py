def f(n):
    bin_n = bin(n)[2:]
    bin_count_1 = bin(bin_n.count('1'))[2:].lstrip('0')
    bin_count_0 = bin(bin_n.count('0'))[2:].lstrip('0')
    res = int(bin_count_0 + bin_count_1, 2)
    return res
for N in range(1, 10000000):

    if f(N) == 123:
        print(N)
        break