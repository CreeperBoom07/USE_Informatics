nodes = 'АБГ БДЕ ВБАГЖ ГЖ ДЗКЕ ЕКВ ЖЕ ЗК ИЖ КИЖ'
d = {c[0]: c[1:] for c in nodes.split()}

def f(s, end):
    if s[-1] == end and len(s) > 1:
        return 1
    return sum(f(s+c, end) for c in d[s[-1]])


print(f('Е', 'Е'))

# 17
