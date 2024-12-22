# +1 *3  win >= 65  s1=6  1<s2<58
#19-> 7
#20-> 10, 19
#21-> 18

i = [2, 4]
rock = 65

def f(s1, s2, pos):
    if s1+s2 >= rock and pos in i: return True
    if s1+s2 <= rock and pos == i[-1]: return False
    if s1+s2 >= rock: return False
    if pos % 2 == i[-1] % 2:
        return all([f(s1+1, s2, pos+1), f(s1*3, s2, pos+1), f(s1, s2+1, pos+1), f(s1, s2*3, pos+1)])
    return any([f(s1+1, s2, pos+1), f(s1*3, s2, pos+1), f(s1, s2+1, pos+1), f(s1, s2*3, pos+1)])


for s2 in range(2, 58):
    if f(6, s2, 0):
        print(s2)