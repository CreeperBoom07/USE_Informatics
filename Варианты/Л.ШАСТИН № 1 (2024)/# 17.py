def prime(n):
    if n < 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

with open('17 (3).txt') as file:
    data = [int(n) for n in file]
    mx = max([n for n in data if str(n).endswith('17')])
lst = []
for x in range(len(data)-1):
    if prime(data[x]) ^ prime(data[x+1]):
        if abs((data[x] + data[x+1])) % mx == 0:
            lst += [data[x]*data[x+1]]
            
print(len(lst), max(lst), sep='\n')
