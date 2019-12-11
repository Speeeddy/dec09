class SystemInformation:
    def __init__(self):
        print(self, 'am in constructor')

    def __del__(self):
        print(self, 'getting destroyed.....')


if __name__ == '__main__':
    si = SystemInformation()
    # del si
    print(si)
