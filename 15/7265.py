def f(x, y, A):
    return (3*x + 2*y > 25) or (x > 2*y) or (x + 4*y < A)

for A in range(1, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not f(x, y, A):
                flag = False
                break
        if not flag:
            break
    if not flag:
        print(A)