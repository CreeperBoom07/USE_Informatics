def f(x):
    d = {1}
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)


for x in range(1204300, 1204380+1):
    d = [i for i in f(x) if i % 2 == 0] 
    if not d:
        continue

    s = sum(d)
    if s!=0 and s%10 == 0:
        print(x, s)
