from re import fullmatch

# for i in range(2023, 10**10, 2023):
#     if fullmatch(r'1\d2139\d*4', str(i)):
#         print(i, i // 2023)

# a = []
# for x in range(10):
#     for y in list(range(1000)) + ['', '00', '000']:
#         n = int(f'1{x}2139{y}4')
#         if n % 2023 == 0:
#             a.append(n)
# a.sort()
# for el in a:
#     print(el, el // 2023)
# 162139404 80148
# 1321399324 653188
# 1421396214 702618
# 1521393104 752048

for i in range(2023, 10**10, 2023):
    n = str(i)
    if n[0] == '1' and n[2:6] == '2139' and n[-1] == '4':
        print(i, i // 2023)