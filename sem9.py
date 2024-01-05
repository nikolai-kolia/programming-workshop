# 4.13
print([len(_) for _ in ['1', '123', '123', '12', '1', '123']])

# 4.14
print(sum([1 if len(_) > 2 else 0 for _ in ['1', '123', '123', '12', '1', '123']]))

# 4.18
print(list(filter(lambda x: x >= 0, [1, 123, -123, 12, -1, 3])))

# 4.19
l1 = [1, 123, -123, 12, -1, 3]
print([_ if _ >= 0 else l1.index(_) for _ in l1])

# 5.2
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

# С одним параметром
result1 = multiply(15)
print(result1)  # Вывод: 15

# С двумя параметрами
result2 = multiply(3, 5)
print(result2)  # Вывод: 15

# С тремя параметрами
result3 = multiply(2, 5, 10)
print(result3)  # Вывод: 100

# 5.3
a1 = (15, 10, 5)
result_a1 = multiply(*a1)
print(result_a1)  # Вывод: 750

a2 = (3, 1)
result_a2 = multiply(*a2)
print(result_a2)  # Вывод: 3

a3 = [2, 35, 55]
result_a3 = multiply(*a3)
print(result_a3)  # Вывод: 3850

a4 = (5, 10, 15, 20)
result_a4_first = multiply(*a4[:3])
print(result_a4_first)  # Вывод: 750

result_a4_last = multiply(*a4[-3:])
print(result_a4_last)  # Вывод: 3000

# 5.8
num_to_text_dict = {
    0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять",
    10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
    16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать",
    40: "сорок", 50: "пятьдесят", 60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят", 90: "девяносто",
    0.1: "десятая", 0.01: "сотая", 0.001: "тысячная",
}


def convert_to_text(number):
    if number in num_to_text_dict:
        print(num_to_text_dict[number])
    else:
        answer = ''
        for _ in range(len(str(number))):
            answer += f'{num_to_text_dict[int(str(number)[_]) * (10 if _ == 0 and len(str(number)) != 1 else 1)]} '
        print(answer[:-1])


convert_to_text(40)

# 5.9
text_to_num_dict = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
    "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
    "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, "двадцать": 20, "тридцать": 30,
    "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90, "сто": 100,
    "двести": 200, "триста": 300, "четыреста": 400, "пятьсот": 500, "шестьсот": 600, "семьсот": 700,
    "восемьсот": 800, "девятьсот": 900, "десятая": 0.1, "сотая": 0.01, "тысячная": 0.001,
}

print(sum([text_to_num_dict[_] for _ in 'тридцать три'.split()]))

# 6.1
def calc(expression):
    if 'плюс' in expression:
        input_list = expression.split(' плюс ')
        operation = '+'
    elif 'минус' in expression:
        input_list = expression.split(' минус ')
        operation = '-'
    elif 'умножить на ' in expression:
        input_list = expression.split(' умножить на ')
        operation = '*'
    elif 'разделить на ' in expression:
        input_list = expression.split(' разделить на ')
        operation = '/'
    elif 'остаток' in expression:
        input_list = expression.split(' остаток ')
        operation = '%'
    num1_text, num2_text = input_list[0], input_list[1]
    num1, num2 = sum([text_to_num_dict[_] for _ in num1_text.split()]), sum([text_to_num_dict[_] for _ in num2_text.split()])
    #print(f"{num1} {operation} {num2}")
    result = eval(f"{num1} {operation} {num2}")
    #print(result)
    convert_to_text(result)


calc("двадцать пять плюс тринадцать")  # Вывод: "тридцать восемь"
calc("тринадцать минус девять")  # Вывод: "четыре"
calc("шесть умножить на семь")  # Вывод: "сорок два"