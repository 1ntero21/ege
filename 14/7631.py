
for x in '123456789ABCDEFGHI':
    number_1 = int(f"98897{x}21", 19)
    number_2 = int(f"2{x}923", 19)
    if (number_1 + number_2) % 18 == 0:
        print(f"{x} -> {(number_1 + number_2) // 18}")