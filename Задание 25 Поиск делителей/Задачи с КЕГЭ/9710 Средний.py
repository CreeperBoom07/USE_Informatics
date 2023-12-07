from fnmatch import *

lst = []

for x in range(1000001268, 10**10, 2023):
    if fnmatch(str(x), '1*1'):
        lst += [x]

lst = sorted(lst, key=lambda x: sum(int(i) for i in str(x)), reverse=True)
lst2 = []
for i in range(5):
    lst2 += [lst[i]/2023]

print(*sorted(lst2), sep='\n')
##839347
##933217
##937217
##988477
##988517
