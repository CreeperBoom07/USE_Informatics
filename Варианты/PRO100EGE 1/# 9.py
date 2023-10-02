with open('./9_10711.csv') as file:
    data = [[int(x) for x in line.split(',')] for line in file]

for line in data:
    d = {}
    for x in line:
        d[x] = d.get(x, 0) + 1
    val = list(d.values())
    if val.count(2) == 2 and val.count(1) == 3:
        if d[max(line)] == 1:
            print(sum(line))
            break
        
        
