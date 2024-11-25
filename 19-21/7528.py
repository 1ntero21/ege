# +1 +4 *2  win >=58  1<=s<=57
#19-> 28
#20-> 14, 24, 27
#21-> 23, 26, 28

def f(s, pos):
    if s >= 58 and pos % 2== 0: return True
    if s <= 58 and  pos == 4: return False
    if s >= 58: return False
    if pos % 2 == 0:
        return f(s+1, pos+1) and f(s+4, pos+1) and f(s*2, pos+1)
    return f(s+1, pos+1) or f(s+4, pos+1) or f(s*2, pos+1)


for s in range(1, 57):
    if f(s, 0):
        print(s)