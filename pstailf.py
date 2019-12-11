def tailf(log_file):
    """log watch"""
    try:
        with open(log_file) as fp:
            # fp.seek(0, 2)   # fp to the eof

            while True:
                content = fp.read(1024)
                if content:
                    yield content
    except FileNotFoundError as err:
        print(err)


if __name__ == '__main__':
    for item in tailf('passwd'):
        print(item)

