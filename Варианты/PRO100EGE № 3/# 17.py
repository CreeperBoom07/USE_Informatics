with open('17_11887.txt') as file:
    data = [int(n) for n in file]

mx = max(n for n in data if abs(n)%100==68)

lst = []
for i in range(len(data)-3):
    dv = [1 for x in (0, 1, 2, 3) if 10 <= abs(data[i+x]) <= 99]
    if len(dv) == 1 or len(dv) == 4:
        if (data[i] + data[i+1] + data[i+2] + data[i+3]) >= mx:
            lst += [data[i] + data[i+1] + data[i+2] + data[i+3]]
print(len(lst), max(lst), sep='\n')
##75
##247177
