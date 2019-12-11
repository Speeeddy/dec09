"""process pool"""

import multiprocessing
from time import sleep


def compute(item):
    p_name = multiprocessing.current_process().name
    sleep(1)
    print(f'{p_name}, rece : {item}')
    return item * item


def main():
    data_set = [1, 2, 3, 7, 4, 5, 4, 3, 5]
    pool = multiprocessing.Pool(3)
    result = pool.map(compute, data_set)
    print(result)

if __name__ == '__main__':
    main()
