with open('17 (4).txt') as file:
    data = [int(n) for n in file]
    mx = max([n for n in data if abs(n) % 10 == 3])
lst = []
for x in range(len(data)-2):
    if sum(abs(data[x+i]) % 2 != 0 for i in [0, 1, 2]) == 1:
        if sum(data[x+i] for i in [0, 1, 2]) >= mx:
            lst += [sum(data[x+i] for i in [0, 1, 2])]
print(len(lst), sum(lst), sep='\n')
