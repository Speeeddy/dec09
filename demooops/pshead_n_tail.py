class HeadAndTail:
    def __init__(self, file_name):
        pass

    def __rshift__(self, other):
        print('tail function')

    def __lshift__(self, other):
        print('head')


ht = HeadAndTail('/etc/passwd')
ht >> 5   # last 5 lines of the file , tail -5 /etc/passwd
print()
ht << 5   # first 5 lines