# Создать словарь d8, в котором есть все пары ключ-значения из d5, а для ключей, которые есть в d6, но отсутствуют в d5
# Добавить соответствующие пары ключ-значения в d8. Использовать генераторы, решить задачу в одну строку.
print(input().upper())
print({**{key: value for (key, value) in {_: _ for _ in range(0, 21, 2)}.items()}, **{key2: value2 if (not (key2 in {_: _ for _ in range(0, 21, 2)})) else {_: _ for _ in range(0, 21, 2)}[key2] for (key1, value1) in {_: _ for _ in range(0, 21, 2)}.items() for (key2, value2) in {_: _ for _ in range(0, 11)}.items()}})