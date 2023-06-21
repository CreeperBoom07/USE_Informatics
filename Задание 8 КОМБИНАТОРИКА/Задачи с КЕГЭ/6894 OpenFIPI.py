from itertools import product as pd


for ind, val in enumerate(pd(sorted('ЦАПЛЯ'), repeat=5), start=1):
    if val.count('А') <= 1 and val.count('Ц') == 2 and 'Л' not in val:
        print(ind)
        break

# 319
