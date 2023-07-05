#Компьютер отгадывает загаднное число

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT = 10

num_input = int(input("Загадайте число от 0 до 1000: "))
num = randint(LOWER_LIMIT, UPPER_LIMIT)

i = 0
limit = UPPER_LIMIT
lower = LOWER_LIMIT
while i < ATTEMPT:
    answer = input(f"Введите номер ответа: число {num}\n1.больше загадного\n2.меньше загаданного\n3.равно загаданному\n")
    if answer == "1" and i != ATTEMPT - 1:
        lower = num
        num = int(num + (limit - num) / 2)
        i += 1
        continue
    elif answer == "2" and i != ATTEMPT - 1:
        limit = num
        num = int(lower + (num-lower)/2)
        i += 1
        continue
    elif answer == "3":
        print(f"Загаданое число = {num}")
        break
    elif answer != "1" and answer != "2" and answer != "3":
        print("Такого варианта нет, попробуйте еще раз")
        continue
    if i == ATTEMPT - 1 and answer != "3":
        print("У меня не получилось отгадать твое число :( Ты отвечал верно? ")
        break