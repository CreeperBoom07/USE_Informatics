with open('17_10719.txt') as file:
    data = [int(n) for n in file]
lst = []
for x in range(len(data)-3):
    if str(data[x]).endswith('13') ^ str(data[x+3]).endswith('13'):
        lst.append(data[x]+data[x+3])
print(len(lst), max(lst), sep='\n')
