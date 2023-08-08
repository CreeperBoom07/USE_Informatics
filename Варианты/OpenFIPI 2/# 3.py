s = 'АБГ БД ВГЖАБД ГЖ ДИЕ ЕВЛ ЖЕ ИЛ КЖ ЛЖК'
nodes = {x[0]: x[1:] for x in s.split()}


def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s+x, end) for x in nodes[s[-1]] if s.count(x) == 0)


print(f('В', 'Е') + f('Л', 'Е'))
