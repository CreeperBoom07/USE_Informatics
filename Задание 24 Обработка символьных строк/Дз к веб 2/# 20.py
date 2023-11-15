s1= '' 
m = 1
k = 0
for s in open('files/24_2507.txt'):
    c = 1
    m_temp = 1
    k += s.count('K')
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            c += 1
            m_temp = max(m_temp, c)
        else:
            c = 1
    if m_temp > m:
        m = m_temp
        s1 = s
d = {x: s1.count(x) for x in sorted(set(s1))}
print(d)
print(k)
#K36582
