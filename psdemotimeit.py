from timeit import timeit


def demo1():
    items = []
    for i in range(10):
        items.append((bin(i), oct(i), hex(i)))

    return items


def demo2():
    return [(bin(i), oct(i), hex(i)) for i in range(10)]


if __name__ == '__main__':
    print(timeit('sin(30)', setup='from math import sin'))
    print(timeit('demo1()', setup='from __main__ import demo1'))
    print(timeit('demo2()', setup='from __main__ import demo2'))
