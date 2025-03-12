from re import *

with open('text') as fin:
    s = fin.readline().strip()

pattern = r'(?:0|[1-9][0-9]*)(?:[*+](?:0|[1-9][0-9]*))*'

arr = [i.group() for i in finditer(pattern, s)]
max_len = len(max(arr, key=len))
arr = [i for i in arr if len(i) == max_len]

max_num = max(eval(i) for i in arr)

print(max_num)