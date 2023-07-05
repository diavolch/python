# ✔Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)

i = 0
while i < ATTEMPT:
    input_num = int(input("Какое число было загадано: "))
    if input_num > num and i != ATTEMPT - 1:
        print("Попробуйте выбрать число меньше")
        i += 1
        continue
    elif input_num < num and i != ATTEMPT - 1:
        print("Попробуйте выбрать число больше")
        i += 1
        continue
    elif input_num == num:
        print(f"Вы угадали! Число = {num}")
        break
    if i == ATTEMPT - 1 and input_num != num:
        print(f"Вы использовали все 10 попыток :( . Было загадано {num}")
        break