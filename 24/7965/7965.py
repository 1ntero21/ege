from re import *

with open('text') as fin:
    s = fin.readline().strip()

pattern = r'(?:0|[1-5][0-5]*)(?:[*+](?:0|[1-5][0-5]*))*'

arr = [i.group() for i in finditer(pattern, s)]

print(len(max(arr, key=len)))
