# №1.2[3]. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# Примеры/Тесты:
#     20 21 22(ввод чисел НЕ в одну строку)  -> Общее кол-во парт будет 32
#     21 21 21(ввод чисел НЕ в одну строку)  -> Общее кол-во парт будет 33



a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
part1 = a // 2 if a % 2 == 0 else a//2 + 1  # Тернарный оператор
part2 = b // 2 if b % 2 == 0 else b//2 + 1
part3 = c // 2 if c % 2 == 0 else c//2 + 1
sumpart = part1 + part2 + part3
print (sumpart)