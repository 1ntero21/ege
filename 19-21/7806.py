# -2 -3 //2  win<=25
#19-> 52
#20-> 54 55
#21-> 57

i = [2, 4]
rock = 25

def f(s, pos):
    if s <= rock and pos in i: return True
    if s >= rock and pos == i[-1]: return False
    if s <= rock: return False
    if pos % 2 == i[-1] % 2:
        return all([f(s-2, pos+1), f(s-3, pos+1), f(s//2, pos+1)])
    return any([f(s-2, pos+1), f(s-3, pos+1), f(s//2, pos+1)])

for s in range(26, 150):
    if f(s, 0):
        print(s)