def get_value(value):
    print(f'recv arg as : {value}')
    return [value ** 2, value ** 3]


g = (get_value(i) for i in range(1, 6))
print(g)

for item in g:
    print(item)
    print('-' * 22)

