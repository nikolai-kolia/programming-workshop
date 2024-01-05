# 1
# s1, s2, s3 = input(), input(), ''
# for x in s1:
#    for y in s2:
#        if x == y:
#            s3 += x
# print(s3)

# 2
# n, ans = int(input()), 1
# while (n > 1 and n != 2):
#    ans *= n
#    n = n - 2
# print(ans)

# 3
# n, ans = int(input()), 1
# for _ in range(n, 1, -2):
#    ans *= _
# print(ans)

# 7
s1, s2 = input().lower(), input().lower()
for x in range(len(s1)):
    for y in s2:
        if s1[x] == y:
            s3 = ''
            indexes = [_ for _ in range(len(s2))]
            for _ in indexes:
                if _ == s2.index(y):
                    s3 += s2[s2.index(y)].upper()
                else:
                    s3 += s2[_]
            print(f'{x + 1} символ встречается в строке поиска: {s3}')
