def div(x):
    d = set()
    for i in range(1, int(x**.5)+1):
        if x % i == 0:
            d.add(i) # Первый делитель
            d.add(x//i) # Второй делитель в паре
            d |= {i, x//i}
    return sorted(d) 
print(div(100_000_000))
