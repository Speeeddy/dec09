keys = ['login', 'uid', 'shell', 'home', 'gecos', 'pwd']
values = ['root', 0, '/bin/bash', '/root', 'administrator']

print(zip(keys, values))
print()
print(list(zip(keys, values)))
print()
print(dict(zip(keys, values)))
