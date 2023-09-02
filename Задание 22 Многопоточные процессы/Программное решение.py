# Перед этим скопировать содержимое таблицы в .txt файл

d = {'0': 0}
data = []
with open('file_name.txt') as file:
    for s in file:
        s = s.replace(';', ' ').split()
        data.append(s)



# Проходим по списку процессов и вясняем их время до тех пор,
# пока не узнаем время каждого из них
while len(d) != len(data)+1:
    # Проходим по списку всех процессоров
    for s in data:
        # Если мы знаем время каждого подпроцесса
        if all(sub in d for sub in s[2:]):
            # Вычисляем итоговое время как время работы + максимум из подпроцессов
            d[s[0]] = int(s[1]) + max(d[sub] for sub in s[2:])
print(max(d.value()))
