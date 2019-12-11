import shelve
# from demooops.psoop3 import PackageManager


with shelve.open('content') as sh:
    for key, value in sh.items():
        print(key, value)

    print()
    # sh['custom'].get_information()