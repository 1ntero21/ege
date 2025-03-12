from re import *

with open('text') as fin:
    s = fin.readline().strip()

pattern = r'(?:0|[1-2][0-2]*)(?:[*+](?:0|[1-2][0-2]*))*'

arr = [i.group() for i in finditer(pattern, s)]

print(len(max(arr, key=len)))
