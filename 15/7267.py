def f(x, y, A):
    return (4*x + y > 115) or (x > 3*y) or (x + 4*y < A)

for A in range(1, 1000):
    flag = True
    for x in range(0, 2000):
        for y in range(0, 2000):
            if not f(x, y, A):
                flag = False
                break
        if not flag:
            break
    if not flag:
        print(A)