m = 0
s = 0
def f(x, y, n):
    if x == y and n.count('2') > n.count('1'):
        return 1
    if x > y:
        return 0
    return f(x+1, y, n+'1') + f(x*2, y, n+'2') + f(x*5, y, n+'2')

print(f(3, 260, ''))
