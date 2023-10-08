abc = '0123456789ABC'
def f(n):
    s = ''
    nn = abs(n)
    while nn:
        s = abc[nn%13] + s
        nn //= 13
        
    return s.endswith('12')
        

with open('17.txt') as file:
    data = [int(num) for num in file]
    mx = max([num for num in data if f(num)])
    
lst = []
for x in range(len(data)-2):
    k = 0
    for i in range(3):
        if 99 < abs(data[x+i]) < 1000:
            k += 1
    if k == 2 and (data[x]+ data[x+1] + data[x+2]) < mx:
        lst.append(data[x]*data[x+1]*data[x+2])
        
print(len(lst), max(lst), sep='\n')
