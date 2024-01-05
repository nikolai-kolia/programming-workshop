# 1
#import re
#
#string = 'aaa--bbb==ccc__ddd'
#result = re.split(r'[-=]{2,}|[_]{2,}', string)
#print(result)

# 2
import re

string = 'Yesterday, All my troubles seemed so far away'
first_word = re.match(r'\b(\w+)\b', string).group(0)
print(first_word)

# 3
import re

string = 'Yesterday, All my troubles seemed so far away'
last_word = re.match(r'\b(\w+)\b', string[::-1]).group(0)
print(last_word[::-1])

# 6
#import re
#
#def check_email(email):
#    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#    return bool(re.match(pattern, email))
#
#emails = [
#    "example@mail.ru",
#    "example@gmail.com",
#    "example@domain.com",
#    "invalid-email",
#    "user@gmail",
#]
#
#for email in emails:
#    print(email, check_email(email))

# 8
import re

def check_number(number):
    pattern = r'^\+7\s?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, number))

numbers = [
    "+7(999)999-99-99",
    "+7 (999) 999-99-99",
    "+7 999 999-99-99",
    "+7 999 999 99 99",
    "+79999999999",
    "89999999999",
    "8(999)999-99-99",
]

for number in numbers:
    print(number, check_number(number))