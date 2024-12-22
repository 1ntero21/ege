# +1 +3 *4  win>=111
#19-> 27
#20-> 24 26
#21-> 23 25

i = [2, 4]
rock = 111

def f(s, pos):
    if s >= rock and pos in i: return True
    if s <= rock and pos == i[-1]: return False
    if s >= rock: return False
    if pos % 2 == i[-1] % 2:
        return all([f(s+1, pos+1), f(s+3, pos+1), f(s*4, pos+1)])
    return any([f(s+1, pos+1), f(s+3, pos+1), f(s*4, pos+1)])

for s in range(1, 111):
    if f(s, 0):
        print(s)