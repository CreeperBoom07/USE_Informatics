def to_decimal(num, osn):
    s = 0
    lenght = len(num)
    for n in range(lenght):
        s += int(num[n]) * osn ** (lenght - n - 1)
    return s

def f1():
    for x in range(0, 17):
        temp = to_decimal(f'9759{x}', 17) + to_decimal(f'3{x}108', 17)
        if temp % 11 == 0:
            print(temp / 11)
            break


f1()

# 95306
