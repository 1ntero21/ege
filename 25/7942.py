from fnmatch import *

for i in range(0, 10**10+1, 18579):
    if fnmatch(str(i), '54?1?3*7'):
        print(i, i //18579)