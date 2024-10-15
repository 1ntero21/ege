print('a b c d')

for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                if (a <= b) and (b <= (not c)) and ((not c) <= d):
                    print(a, b, c, d)
# a b c d
# 0 0 0 1
# 0 0 1 1

# 0 1 0 1 True 2
# 1 1 0 1 True 3

# d c b a