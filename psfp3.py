items = list(range(1, 200))
print(items)
print()

m = map(lambda n: (n, n % 7 == 0), items)
print(list(m))
print()

# m = filter(lambda : n % 7 == 0, items)
# print(m)
# print(list(m))
# print()
