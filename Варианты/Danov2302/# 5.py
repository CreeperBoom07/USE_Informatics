for n in range(5, 1000):
    R = bin(n)[2:]
    lenght = len(R)
    if lenght % 2 != 0:
        R = R[:lenght//2] + str(1 - int(R[lenght//2])) + R[lenght//2+1:]
    else:
        R = R[:lenght//2-1] + str(1 - int(R[lenght//2-1])) + str(1 - int(R[lenght//2])) + R[lenght//2+1:]
    if int(R, 2) > 100 and int(R, 2) < n:
        print(n, R)

# 7
        
