print(range(10))

# r = iter(range(10))
# print(r)
# print(next(r))
from pprint import  pprint as pp

items = [hex(item) for item in range(10)]   # list comprehension
print(items)
print()

items = [i ** i for i in range(10)]   # list comprehension
print(items)
print()

items = [(bin(i), oct(i), hex(i)) for i in range(10)]   # list comprehension
pp(items)
print()
