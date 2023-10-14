with open('9_6925.csv') as file:
    data = [[int(n) for n in line.split(',')] for line in file]
k = 0
for line in data:
    p = [n for n in line if line.count(n) == 2]
    np = [n for n in line if line.count(n) == 1]
    ch = [n for n in line if n % 2 == 0]
    nch = [n for n in line if n % 2 != 0]
    if len(ch) == 0:
        sr_ch = 0
    else:
        sr_nch = sum(nch) / len(nch)
    if len(nch) == 0:
        sr_nch = 0
    else:
        sr_ch = sum(ch) / len(ch)

    if (len(p) == 2 and len(np) == 4) ^ (abs(sr_ch - sr_nch) > 50):
        k += 1
print(k)

# 862
