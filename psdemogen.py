def get_integers():
    """infinite stream"""
    i = 1

    while True:
        yield i
        i += 1


square = (item ** 2 for item in get_integers())

print(next(square))
print(next(square))