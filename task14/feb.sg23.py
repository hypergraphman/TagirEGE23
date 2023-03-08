for p in range(10, 36):
    for x in range(1, 36):
        for y in range(1, 36):
            if 3 * p ** 3 + 2 * p ** 2 + x * p + 8 + x * p ** 3 + x * p ** 2 + x * p + 9 == y * p ** 3 + y * p ** 2 + 2:
                print(y * p ** 2 + y * p + x)
