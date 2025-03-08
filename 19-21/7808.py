# +1 +2 *3  win>=163
#19-> 17
#20-> 43 50
#21-> 49

i = [3]
rock = 163

def f(s1, s2, pos):
    if s1 + s2 >= rock and pos in i: return True
    if s1 + s2 <= rock and pos == i[-1]: return False
    if s1 + s2 >= rock: return False
    if pos % 2 == i[-1] % 2:
        return all([f(s1+1, s2, pos+1), f(s1+2, s2, pos+1), f(s1*3, s2, pos+1), f(s1, s2+1, pos+1), f(s1, s2+2, pos+1), f(s1, s2*3, pos+1)])
    return any([f(s1+1, s2, pos+1), f(s1+2, s2, pos+1), f(s1*3, s2, pos+1), f(s1, s2+1, pos+1), f(s1, s2+2, pos+1), f(s1, s2*3, pos+1)])

for s in range(1, 151):
    if f(11, s, 0):
        print(s)