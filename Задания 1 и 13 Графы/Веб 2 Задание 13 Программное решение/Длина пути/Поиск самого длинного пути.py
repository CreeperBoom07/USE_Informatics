"""Самый длинный путь из А -> М"""
nodes = 'АБВГД БЕВ ВЖ ГВЖ ДГЖЗ ЕЖИ ЖИ ЗЖИ ИКЛ КМ ЛКМ'
d = {c[0]: c[1:] for c in nodes.split()}


def f(s, end):
    if s[-1] == end:
        return len(s)-1  # Возвращаем длину пути
    return max(f(s+c, end) for c in d[s[-1]])


print(f('А', 'М'))

# 8
