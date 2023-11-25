def f(x):
    d = set()
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(850_001, 850_100):
    d = f(x)
    if d:
        F = max(d) - min(d)
    if F != 0 and F % 3 == 0:
        print(x, F)
     
##850003 121422
##850005 283332
##850006 425001
##850012 425004
##850015 169998
##850018 425007
