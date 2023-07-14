"""Указать первый путь в лексикографическом порядке из города А в Н,
   содержащий ровно 8 городов, включая А и Н"""

nodes = 'АБГД БВГ ВЗКЕ ГВЕЖ ДГ ЕКМИЖ ЖИ ЗЛК ИМ КЛНМ ЛН МН'
d = {c[0]: c[1:] for c in nodes.split()}

lst = []

def f(s, end):
    if s[-1] == end:
        lst.append(s) if len(s) == 8 else ...
        return 1
    return sum(f(s+x, end) for x in d[s[-1]])

print(f('А', 'Н'))
print(sorted(lst)[0])

# АБВЕЖИМН
