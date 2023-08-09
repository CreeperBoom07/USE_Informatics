def f(line):
    c = 0
    nc = 0
    for n in line:
        if n % 2 == 0:
            c += 1
        else:
            nc += 1
    return c > nc

with open('./9_5946.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]

k = 0
for line in data:
    if len(set(line)) == 6 and f(line):
        k += 1
print(k)

# 1078


    
