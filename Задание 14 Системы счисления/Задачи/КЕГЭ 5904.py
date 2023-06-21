from string import ascii_uppercase as a_u
s = '0123456789' + a_u
s = s[:20]

max_sum = -1
def sem_osn(num):
    s = 0
    while num:
        s += num % 7
        num //= 7
    return s


def generator_loops():
    for x in range(1, 20):
        for y in range(0, 5):
            yield x, y


for x, y in generator_loops():
    X = s[x]
    Y = s[y]
    n1 = int(f'{X}1{X}2{X}3{X}4', 20)
    n2 = int(f'1{Y}2{Y}3{Y}4{Y}', 5)
    num = sem_osn(n1-n2)
    if num > max_sum:
        max_sum = num

print(max_sum)

# 56
