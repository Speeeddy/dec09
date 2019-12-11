from json import load
from pprint import pprint as pp


with open('tmp.json') as fp:
    content = load(fp)

    for dir_name, dir_content in content.items():
        print(dir_name)
        for file_name, file_prop in dir_content.items():
            print("\t", file_name)

            for prop_name, value in zip(['size', 'mtime'], file_prop):
                print(f'\t\t {prop_name}: {value}')
            print()