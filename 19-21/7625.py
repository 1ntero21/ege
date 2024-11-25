# -2 - 5 //3  win <= 19  s >= 20
#19-> 60, 61
#20-> 62, 63
#21-> 64

def f(s, pos):
    if s <= 19 and pos % 2== 0: return True
    if s >= 19 and pos == 4: return False
    if s <= 19: return False
    if pos % 2 == 0:
        return f(s-2, pos+1) and f(s-5, pos+1) and f(s//3, pos+1)
    return f(s - 2, pos + 1) or f(s - 5, pos + 1) or f(s // 3, pos + 1)


for s in range(20, 100):
    if f(s, 0):
        print(s)