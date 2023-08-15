R = bin(11)[2:]
lenght = len(R)
if lenght % 2 != 0:
    R = R[:lenght//2] + str(1 - int(R[lenght//2])) + R[lenght//2+1:]
else:
    R = R[:lenght//2-1] + str(1 - int(R[lenght//2-1])) + str(1 - int(R[lenght//2])) + R[lenght//2+1:]
print(int(R, 2))
