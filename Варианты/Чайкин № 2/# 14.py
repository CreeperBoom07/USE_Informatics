from string import ascii_uppercase as UP

abc = '0123456789' + UP
abc = abc[:18]
for x in abc:
    n1 = int(f'973F8{x}24', 18)
    n2 = int(f'7241{x}1E5', 18)
    n3 = int(f'31{x}154C', 18)
    if (n1+n2+n3) % 11 == 0:
        print((n1+n2+n3) / 11)
# 929218839
