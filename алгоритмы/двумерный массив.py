# a = []
# for i in range(4):
#     b = []
#     for j in range(3):
#         b.append(str(i) + str(j))
#     a.append(b)

a = [[str(i) + str(j) for j in range(3)] for i in range(4)]

print(a)