for x in range(0, 98):
    n1 = 1*98**4 + 2*98**3 + x*98**2 + 4*98 + 5
    n2 = 1*123**3 + x*123**2 + 9*123 + 8
    if (n1+n2) % 123 == 0:
        print(x, (n1+n2) / 123)

# 792604
