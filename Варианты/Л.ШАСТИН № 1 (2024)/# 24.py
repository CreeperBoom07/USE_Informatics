with open('24 (2).txt') as file:
    s = file.readline()
k = 0
l = False
c = 0
for x in s:
    if l and x != 'A':
        c += 1
    if x == 'A' and not l:
        l = True
    elif x == 'A' and l and c > 0:
        k += 1
        c = 0
    
print(k)        
