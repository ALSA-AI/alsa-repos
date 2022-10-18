plus = []
minus = []
div = []
multy = []
i = 1
while i != 0:
    a = int(input("Введите первое число:"))
    b = int(input("Введите второе число:"))
    c = input("Оператор(+-/*):")
    print()
    if c == '+':
        res = a + b
        print(f"{a} + {b} = {res}")
        plus.append(f"{a} + {b} = {res}")

    elif c == '-':
        res = a - b
        print(f"{a} - {b} = {res}")
        minus.append(f"{a} - {b} = {res}")

    elif c == '/':
        res = a / b
        print(f"{a} / {b} = {res}")
        div.append(f"{a} / {b} = {res}")

    elif c == '*':
        res = a * b
        print(f"{a} * {b} = {res}")
        multy.append(f"{a} * {b} = {res}")

    print("+", plus)
    print("-", minus)
    print("/", div)
    print("*", multy)
