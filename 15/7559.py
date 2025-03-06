def f(x, A):
    return (x % 33 == 0) <= ((x % A !=0) <= (x % 242 != 0))

for A in range(1, 10000):
    flag = True
    for x in range(1, 2000):
        if not f(x, A):
            flag = False
            break
    if flag:
        print(A)