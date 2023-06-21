def f(l, cg, csg):
    if l == 18:
        return cg == csg
    '''    гласные              согласные'''
    return f(l+1, cg+1, csg)*3+f(l+1, cg, csg+1)*5


print(f(8, 4, 4))
