'''При каком наименьшем натуральном значении переменной х
   в выражении 81**20 - 9**x + 50 сумма цифр в 9-ричной записи числа равна 138'''
def f(num):
    s = 0
    while num:
        s += num % 9
        num //= 9
    if s == 138:
        return True
    return False

for x in range(2, 30):
    n = 81**20 - 9**x + 50
    if f(n):
        print(x)
        break
