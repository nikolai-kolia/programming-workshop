from random import randint
from itertools import permutations

p = permutations('0123456789', r=4)
start = ''.join(list(p)[randint(0, 5040)])
counts_of_attempts = 0
print('Правила игры: цифры не повторяются, ноль может быть на первом месте')
while True:
    counts_of_attempts += 1
    predict = input('Вводите очередной вариант отгадываемого числа: ')
    if (not predict.isdigit()) and len(predict) != 4:
        print('Некорректный формат ввода!')
        continue
    bulls = 0
    cows = 0
    for _ in range(4):
        if predict[_] == start[_]:
            bulls += 1
        elif predict[_] in start:
            cows += 1
    if bulls == 4:
        print(f'Ты победил! Количество ходов: {counts_of_attempts}')
        break
    else:
        print(f'Количество коров: {cows}')
        print(f'Количество быков: {bulls}')
