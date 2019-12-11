import shelve
# from demooops.psoop3 import PackageManager

data_set = [1, 2, 3, 7, 4, 5, 4, 3, 5]
s = 'this is a sample string in python'
items = dict(lang='perl', author='larry', release='parrot')
# pm = PackageManager('cpan', '2.2.2')

with shelve.open('content') as sh:
#     sh['custom'] = pm
    sh['string'] = s
    sh['lang'] = items
    sh['elements'] = items

