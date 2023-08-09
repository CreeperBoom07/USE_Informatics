def f(line):
    d = {}
    for n in line:
        d[n] = d.get(n, 0) + 1
        
    vals = list(d.values())
    return vals.count(3) == 1 and vals.count(1) == 3


with open('./9_5284.csv') as file:
    data = [[int(num) for num in line.split(',')] for line in file]

k = 0
for line in data:
    line = sorted(line)
    if (line[0]+line[-1])**2 > line[1]**2 + line[2]**2 + line[3]**2 + line[4]**2:
        k += 1
    elif f(line):
        k += 1
print(k)
        
