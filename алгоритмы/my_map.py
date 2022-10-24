def my_map(func, it):
    r = []
    for el in it:
        r.append(func(el))
    return r


a = '1234'
print(my_map(int, a))

# def my_func(x):
#     return '*' + x + '!'
# my_func = lambda x: '*' + x + '!'
print(my_map(lambda x: '*' + x + '!', ['234', 'asdf', '']))
