alh = '0123456789AB'

for x in alh:
    number_1 = int(f"9A87{x}21", 12)
    number_2 = int(f"2{x}68", 14)
    number_3 = int(f"1{x}2F4", 16)
    if (number_1 + number_2 - number_3) % 3 == 0:
        print(f"{x} -> {(number_1 + number_2 - number_3) // 3}")