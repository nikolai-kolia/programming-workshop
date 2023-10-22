text_to_num_dict = {
    "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
    "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
    "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19, "двадцать": 20, "тридцать": 30,
    "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90,
    "десятая": 0.1, "сотая": 0.01, "тысячная": 0.001,
}
num_to_text_dict = {
    0: "ноль", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять",
    10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
    16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать",
    40: "сорок", 50: "пятьдесят", 60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят", 90: "девяносто",
    0.1: "десятая", 0.01: "сотая", 0.001: "тысячная",
}


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
    result = eval(f"{num1} {operation} {num2}")
    print(result)
    convert_to_text(result)


def convert_to_text(number):
    answer = ''
    for _ in range(len(str(number))):
        answer += f'{num_to_text_dict[int(str(number)[_]) * (10 if _ == 0 and len(str(number)) != 1 else 1)]} '
    print(answer[:-1])


calc("двадцать пять плюс тринадцать")  # Вывод: "тридцать восемь"
calc("тринадцать минус девять")  # Вывод: "четыре"
calc("шесть умножить на семь")  # Вывод: "сорок два"
