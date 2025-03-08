# +3 +6 *3  win>=132
#19-> 41
#20-> 14 35
#21-> 32

i = [2, 4]
rock = 132

def f(s, pos):
    if s >= rock and pos in i: return True
    if s <= rock and pos == i[-1]: return False
    if s >= rock: return False
    if pos % 2 == i[-1] % 2:
        return all([f(s+3, pos+1), f(s+6, pos+1), f(s*3, pos+1)])
    return any([f(s+3, pos+1), f(s+6, pos+1), f(s*3, pos+1)])

for s in range(1, 131):
    if f(s, 0):
        print(s)