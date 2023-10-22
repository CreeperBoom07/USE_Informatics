def tr(x):
    b = ''
    while x:
        b = str(x % 3) + b
        x //= 3
    return b

def sm(el): 
    return sum(int(c) for c in el)

res = []
for n in range(1, 100000):
    b = tr(n)
    if sm(b) % 4 == 0:
        b = '1' + b
        b = b[:-2]
    else: 
        b += tr( sm(b) % 4 * 3 )
    r = int(b, 3)
    if r > 353:
        res += [r]
print(min(res))
