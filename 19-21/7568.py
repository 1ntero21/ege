# +1 *2 win >=227  s1=17  1<=s<=209
#19-> 53
#20-> 96, 104
#21-> 95, 103

def f(s1, s2, pos):
    if s1 + s2 >= 227 and pos % 2 == 0: return True
    if s1 + s2 <= 227 and pos == 4: return False
    if s1 + s2 >= 227: return False
    if pos % 2 == 0:
        return f(s1+1, s2, pos+1) and f(s1*2, s2, pos+1) and f(s1, s2+1, pos+1) and f(s1, s2*2, pos+1)
    return f(s1+1, s2, pos+1) or f(s1*2, s2, pos+1) or f(s1, s2+1, pos+1) or f(s1, s2*2, pos+1)


for s2 in range(1, 210):
    if f(17, s2, 0):
        print(s2)