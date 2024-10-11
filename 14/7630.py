number = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 5*25**4 - 2025
count = 0
while number:
    if number % 25 == 0:
        count += 1
    number //= 25
print(count)