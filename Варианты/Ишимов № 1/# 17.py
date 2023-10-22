with open('17 (2).txt') as file:
    data = [int(n) for n in file]
    dv = min(n for n in data if 10 <= abs(n) < 100)**2
    ch = max(n for n in data if 1000 <= abs(n) < 10000 and n%10==1)
lst = []
for x in range(len(data)-2):
    n1 = data[x]
    n2 = data[x+1]
    n3 = data[x+2]
    if len([i for i in (n1, n2, n3) if i > dv]) == 2:
        if (abs(n1)*abs(n2)*abs(n3)) % ch == 0:
            lst += [abs(n1)+abs(n2)+abs(n3)]
            
print(len(lst), max(lst), sep='\n')
