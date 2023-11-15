from itertools import product as pd
k = 0 
for x in pd([1, 2, 3, 4, 5], repeat=4):
    if sum(x) == 5:
        k += 1
print(k)
# 4
