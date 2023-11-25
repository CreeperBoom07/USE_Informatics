def f(x):
    d = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(333_555, 777_999+1):
    d = [n for n in f(x) if 10 <= n <=99]
    if len(d) == 35:
        print(min(d), max(d))
## 10 96
## 10 99
## 10 99
## 10 91
## 10 99
