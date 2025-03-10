from re import *

with open('text') as fin:
    s = fin.readline().strip()

pattern = r'([789][0789]*)([-*]([789][0789]*))*'
arr = [i.group() for i in finditer(pattern, s)]

print(len(max(arr, key=len)))