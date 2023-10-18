with open('17 (1).txt') as file:
    data = [int(n) for n in file]
    mx = max([n for n in data if str(n).endswith('127')])
lst = []
for x in range(len(data)-2):
    if data[x] < data[x+1] < data[x+2]:
        if (data[x] + data[x+1] + data[x+2]) % mx == 0:
            lst += [data[x] + data[x+1] + data[x+2]]
print(len(lst), max(lst), ' ', *lst, sep='\n')
