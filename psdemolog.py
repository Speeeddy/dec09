from pslogrolloversconfig import logger
from time import sleep


def demo():
    for item in range(1, 11):
        logger.debug(f'dummy messgaes : {item}')
        sleep(.5)


if __name__ == '__main__':
    demo()