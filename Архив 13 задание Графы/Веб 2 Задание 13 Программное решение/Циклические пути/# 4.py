nodes = 'АБ БВ ВЖЕГ ГЕД ДЕЖК ЕЖ ЖНЗ ЗЛКД КЛ ЛМ МАНЗ НАБВ'
d = {c[0]: c[1:] for c in nodes.split()}


def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s+c, end) for c in d[s[-1]] if c not in s)


print(f('Н', 'Ж') + f('З', 'Ж'))

# 69
