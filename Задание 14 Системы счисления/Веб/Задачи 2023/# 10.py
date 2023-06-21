for n in range(1, 100):
    if 3 ** 3 <= n < 3 ** 4 and 7 ** 2 <= n < 7 ** 3 \
            and (n % 8 == 7 and n % 64 // 8 == 1):
        print(n)
        break
# Ответ 79
