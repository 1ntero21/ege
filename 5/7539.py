def f(bin_n):
    sum_num_bin = int(bin_n.count('1')) % 2
    return int(bin_n + str(sum_num_bin), 2)

arr = []
for N in range(1, 10000):
    if f(bin(f(bin(N)[2:]))[2:]) > 75:
        arr.append(f(bin(f(bin(N)[2:]))[2:]))
print(min(arr))