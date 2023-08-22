s = 'АВ БАД ВЕ ГВДБ ДЗ ЕЖ ЖГК ЗЖ КЗ'
d = {x[0]: x[1:] for x in s.split()}


def f(s, end):
    if s[-1] == end:
        return len(s)
    return max(f(s+x, end) for x in d[s[-1]] if s.count(x) == 0)

print(max(f('Г', 'Ж'), f('К', 'Ж')))
# 6
