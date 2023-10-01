nodes = 'АЗВ БГА ВЗКЕБ ГА ДГА ЕБ ЖИ ЗИЖК ИД КЕЖ'  # Указываем все вершины
d = {c[0]: c[1:] for c in nodes.split()}
print(d)


def f(s, end):
    if s[-1] == end:
        return 1
    return sum(f(s+c, end) for c in d[s[-1]])


# Идём из тех узлов, из которых можно попасть в А
print(f('В', 'А') + f('З', 'А'))

# 24
