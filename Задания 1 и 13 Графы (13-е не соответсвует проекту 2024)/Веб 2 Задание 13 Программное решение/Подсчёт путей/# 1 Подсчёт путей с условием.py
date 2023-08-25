"""Проходим через город Ж, но не проходим через город З"""


nodes = 'АБГДЕ БВ ВИЖ ГБВЖД ДЗЖ ЕДЗК ЖЛ ЗЖЛ ИЖЛ КЗЛМ МЛ'
d = {c[0]: c[1:] for c in nodes.split()}


def f(s, end):
    if s[-1] == end:
        # print(s)  # Один из путей
        # Условие
        return 'Ж' in s and 'З' not in s
    return sum(f(s+c, end) for c in d[s[-1]])


print(f('А', 'Л'))

# 10
