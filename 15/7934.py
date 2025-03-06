def f(x, y, A):
    return  (x - 3*y < A) or (y > 400) or (x > 56)

for A in range(0, 1000):
    flag = True
    for x in range(1, 2000):
        for y in range(1, 2000):
            if not f(x, y, A):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)
        break