import time
from time import sleep


def say_after(delay, what):
    sleep(delay)
    print(what)


def main():
    print(f"started at {time.strftime('%X')}")
    say_after(2, 'hello')  # serial
    say_after(3, 'world')
    print(f"finished at {time.strftime('%X')}")


# print(main())
if __name__ == '__main__':
    main()
