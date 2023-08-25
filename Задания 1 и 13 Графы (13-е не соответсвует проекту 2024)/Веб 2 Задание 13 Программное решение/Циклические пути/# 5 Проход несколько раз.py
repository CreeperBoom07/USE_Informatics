"""Проходим через промежуточные города не более 2-ч раз"""
nodes = 'АВ БАГЖ ВДБ ГЖ ДЗ ЗБВ ЖЗД'
d = {c[0]: c[1:] for c in nodes.split()}


def f(s , end):
    if s[-1] == end:
        return 1
    return sum(f(s+c, end) for c in d[s[-1]] if s.count(c) <= 1)


print(f('Ж', 'Г'))

#  36
