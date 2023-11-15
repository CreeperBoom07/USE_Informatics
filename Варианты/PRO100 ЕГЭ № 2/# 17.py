with open('17_11460.txt') as file:
    d = [int(n) for n in file]
    mx = max([n for n in d if str(abs(n))[0] == '8'])

lst = []
for x in range(len(d) - 2):
    if len([n for n in (d[x], d[x+1], d[x+2]) if str(abs(n))[0] == '6']) <= 1:
        if (d[x] + d[x+1] + d[x+2]) >= mx:
            lst += [d[x] + d[x+1] + d[x+2]] 
print(len(lst), min(lst), sep='\n')
#186
#89990
