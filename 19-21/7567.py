# +1 +3 *2 win >=39  1<=s<=38
#19-> 19
#20-> 16, 18
#21-> 15, 17, 19

def f(s, pos):
    if s >= 39 and pos % 2== 0: return True
    if s <= 39 and pos == 4: return False
    if s >= 39: return False
    if pos % 2 == 0:
        return f(s+1, pos+1) and f(s+3, pos+1) and f(s*2, pos+1)
    return f(s + 1, pos + 1) or f(s + 3, pos + 1) or f(s * 2, pos + 1)


for s in range(1, 39):
    if f(s, 0):
        print(s)