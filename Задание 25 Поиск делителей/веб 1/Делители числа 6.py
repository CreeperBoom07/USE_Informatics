def f(x):
    d = set()
    for i in range(2, int(x**.5)+1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for x in range(1_500_001, 1_500_100):
    d = f(x)
    if d:
        F = sum(d) // len(d)
    if F % 10 == 9:
        print(x, F)

## 1500004 64049
## 1500017 10829
## 1500018 123639
## 1500019 123639
## 1500039 74729
