"""Проходим через Г или Е, но не через оба этих пункта"""
nodes = 'АБГД БВГ ВЗКЕ ГВЕЖ ДГ ЕКИ ЖЕИ ЗЛК ИМ КЛНМ ЛН МН'
d = {c[0]: c[1:] for c in nodes.split()}


def f(s, end):
    if s[-1] == end:
        return ('Г' in s and 'Е' not in s) or ('Г' not in s and 'Е' in s)
    return sum(f(s+c, end) for c in d[s[-1]])


print(f('А', 'Н'))

# 28
