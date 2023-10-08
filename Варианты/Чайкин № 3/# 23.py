def f(x, y, s):
    if x > y:
        return 0
    if x == y and s.endswith('BAB'):
        return 1
    return f(x+1, y, s + 'A') + f(x*2, y, s+'B') + f(x+5, y, s+'C')

print(f(5, 62, ''))
