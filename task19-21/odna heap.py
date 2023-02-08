turns = [lambda x: x + 2, lambda x: x * 3]
w = 65
table = {0: set(range(w, 200))}
for i in range(w - 1, 0, -1):
    future = []
    for turn in turns:
        for key in table:
            if turn(i) in table[key]:
                future.append(key)
                break
    even = list(filter(lambda x: x % 2 == 0, future))
    if even:
        if (min(even) + 1) in table:
            table[min(even) + 1].add(i)
        else:
            table[min(even) + 1] = {i}
    else:
        if (max(future) + 1) in table:
            table[max(future) + 1].add(i)
        else:
            table[max(future) + 1] = {i}
print(table[2], table[3], table[4])