# +1 *2  win>=61
#19-> 11
#20-> 15 29
#21-> 57

i = [1, 3]
rock = 61

def f(s, pos):
    if s > 80: return False
    if s >= rock and pos in i: return True
    if s <= rock and pos == i[-1]: return False
    if s >= rock: return False
    if pos % 2 == i[-1] % 2:
        return all([f(s+1, pos+1), f(s*2, pos+1)])
    return any([f(s+1, pos+1), f(s*2, pos+1)])

count = 0
for s in range(1, 61):
    if f(s, 0):
        print(s)
        count += 1
