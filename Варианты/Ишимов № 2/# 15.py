def f(x, y):
    return (not(2*x < 2*a + 3*y)) or (y < 5) or (y >= 18) or (x < 87)

for a in range(1000):
    if all(f(x, y) for y in range(0, 350) for x in range(0, 350)):
        print(a)
        
# 61
