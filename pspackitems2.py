from itertools import zip_longest
import xml
import os


keys = ['login', 'uid', 'shell', 'home', 'gecos', 'pwd']
values = ['root', 0, '/bin/bash', '/root', 'administrator', 'xyz', 'abc']

for item in zip(keys, values):  # parallel iteration
    print(item)

#print(zip_longest(keys, values))
# print()
# print(list(zip_longest(keys, values, fillvalue='')))
# print()
# print(dict(zip_longest(keys, values, fillvalue='')))
