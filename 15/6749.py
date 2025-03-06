def f(x, y, A):
    return  (x + 2*y > A) or (y < x) or (x < 30)

for A in range(0, 1000):
    flag = True
    for x in range(0, 2000):
        for y in range(0, 2000):
            if not f(x, y, A):
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)