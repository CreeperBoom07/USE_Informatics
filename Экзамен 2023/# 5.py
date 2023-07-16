def tr(x: int) -> str:
    s = ''
    while x:
        s = str(x%3) + s
        x //= 3
    return s

lst = []
for n in range(1, 1000):
    r = tr(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += tr((n % 3) * 5)
    if int(r, 3) > 133:
        lst.append(int(r, 3))
        # print(n, int(r, 3))
print(min(lst))
# 141
