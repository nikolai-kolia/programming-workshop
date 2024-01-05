# 2
for x in range(-5, 7):
    print(x, ((x ** 2 > (6 - x)) * (x > 0)))

# 4
s1 = 'string'
s2 = 'String'
s3 = 'strinG'
s4 = 'stringlong'
s5 = ' string'
s6 = 'string '
s7 = '_string'
print(s5<s2<s7<s3<s1<s6<s4)

# 5
s = input()
if "!!!" in s and '???' in s:
    pass
elif '???' in s:
    print('question')
elif "!!!" == s[0:3]:
    print('Nota bene: ')
elif "!!!" in s:
    print('exclaim')
else:
    print('random')