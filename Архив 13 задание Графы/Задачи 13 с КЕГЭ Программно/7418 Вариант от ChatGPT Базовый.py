nodes = 'АГБ БД ВГАБД ГЖЕ ДЕЛИ ЕЛВ ЖЕ ИЛ КЖ ЛКЖ'
d = {c[0]: c[1:] for c in nodes.split()}


def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s + c, end) for c in d[s[-1]] if s.count(c) == 0)


print(f('Л', 'Е') + f('В', 'Е'))

# 21
