"""Ровно 7 городов"""


nodes = 'АБГД БВГ ВИЕГ ГЕЖД ДЖ ЕИМК ЖЕК ИМ КМ'
d = {c[0]: c[1:] for c in nodes.split()}


def f(s, end):
    if s[-1] == end:
        return len(s) == 7
    return sum(f(s+c, end) for c in d[s[-1]])


print(f('А', 'М'))

# 10
