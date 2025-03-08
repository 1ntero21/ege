# -2 -4 //3  win<=40
#19-> 123
#20-> 125 126
#21-> 129

i = [2, 4]
rock = 40

def f(s, pos):
    if s <= rock and pos in i: return True
    if s >= rock and pos == i[-1]: return False
    if s <= rock: return False
    if pos % 2 == i[-1] % 2:
        return all([f(s-2, pos+1), f(s-4, pos+1), f(s//3, pos+1)])
    return any([f(s-2, pos+1), f(s-4, pos+1), f(s//3, pos+1)])

for s in range(41, 1000):
    if f(s, 0):
        print(s)