with open('9.csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]

s = 0
k = 1
for line in data:
    mn = min(line)
    mx = max(line)
    d = {}
    for key in line:
        d[key] = d.get(key, 0) + 1
    val = list(d.values())
    if val.count(3) == 1 and val.count(1) == 4:
        for key in d:
            if d[key] == 3:
                if key != mn and key != mx:
                    s += k
    k += 1
print(s)
    
