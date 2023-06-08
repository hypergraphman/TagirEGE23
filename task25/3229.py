for i in '0123456789':
    for j in '0123456789':
        s = int('12345' + i + '6' + j + '8')
        if s % 17 == 0:
            print(s, s // 17)