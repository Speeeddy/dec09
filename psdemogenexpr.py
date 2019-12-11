items = [11, 22, 33]

t = [i + i for i in items]
print(t)
print()

t = (i + i for i in items)  # GENERATOR expression
print(t)
print(type(t))
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))

for item in t:
    print(item)