# +1 +3 *2  win>=174
#19-> 39 (77)
#20-> 74 76
#21-> 75

i = [2, 4]
rock = 174

def f(s1, s2, pos):
    if s1 + s2 >= rock and pos in i: return True
    if s1 + s2 <= rock and pos == i[-1]: return False
    if s1 + s2 >= rock: return False
    if pos % 2 == i[-1] % 2:
        return all([f(s1+1, s2, pos+1), f(s1+3, s2, pos+1), f(s1*2, s2, pos+1), f(s1, s2+1, pos+1), f(s1, s2+3, pos+1), f(s1, s2*2, pos+1)])
    return any([f(s1+1, s2, pos+1), f(s1+3, s2, pos+1), f(s1*2, s2, pos+1), f(s1, s2+1, pos+1), f(s1, s2+3, pos+1), f(s1, s2*2, pos+1)])

for s in range(1, 111):
    if f(19, s, 0):
        print(s)