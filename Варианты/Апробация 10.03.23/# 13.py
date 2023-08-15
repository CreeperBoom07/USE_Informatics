s = 'АБГ БД ВЖГАБД ГЖ ДИЕ ЕЛКВ ЖЕ ИЕЛ КЖ ЛК'
d = {x[0]: x[1:] for x in s.split()}


def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s+x, end) for x in d[s[-1]] if s.count(x) == 0)

print(f('Л', 'Е') + f('К', 'Е') + f('В', 'Е'))
