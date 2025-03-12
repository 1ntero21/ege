from re import *

with open('text') as fin:
    s = fin.readline().strip()

pattern = r'(?:[1-9A-F][0-9A-F]*)(?:[*+](?:0|[1-9A-F][0-9A-F]*))*'

arr = [i.group() for i in finditer(pattern, s)]

print(len(max(arr, key=len)))