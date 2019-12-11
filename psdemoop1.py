def demo():
    """generator function"""
    print('before 1')
    yield 123
    print('after 1')

    print('before 2')
    yield 12.21
    print('after 23')

    print('before 3')
    yield 'pam'
    print('after 3')


if __name__ == '__main__':
    g = demo()
    for item in g:
        print(item)
        print('-' * 22)
    # print(g)
    # print()
    # print(next(g))
    # print('-' * 22)
    # print(next(g))
    # print('-' * 22)
    # print(next(g))
    # print('-' * 22)
    # print(next(g))
