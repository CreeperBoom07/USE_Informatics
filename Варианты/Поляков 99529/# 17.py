def f(num):
    r = 0
    chet = 0
    nechet = 0
    while num:
       if r % 2 == 0:
           chet += num % 10
       else:
           nechet += num % 10
       num //= 10
       r += 1
    return chet != 0 and nechet % chet == 0


with open('17.txt') as file:
    data = [int(num) for num in file]
    print(data[0])
lst = []
for t in range(0, len(data)-2):
    if f(data[t]) and f(data[t+1]) and f(data[t+2]):
        lst.append(data[t] + data[t+1] + data[t+2])
print(len(data), min(data), sep='\n')
    

