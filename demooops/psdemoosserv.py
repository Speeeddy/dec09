from os import listdir
from os.path import isdir, isfile,  getsize, getmtime, join
from time import ctime

dir_path = '/tmp'

item = listdir(dir_path)[-1]
abs_path = join(dir_path, item)
print(abs_path)
print()
print(isfile(abs_path))
print(isdir(abs_path))
print()
print(getsize(abs_path))
print(getmtime(abs_path))
print(ctime(getmtime(abs_path)))
