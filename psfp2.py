
ascii_values = [112, 101, 116, 101, 114, 32, 112, 97, 110]

"""
112

<ascii char="p">112</ascii>
"""


def tag_it(av):
    """compile time function"""
    return f'<ascii char="{chr(av)}">{av}</ascii>'


tags = map(tag_it, ascii_values)
tags = map(lambda av: f'<ascii char="{chr(av)}">{av}</ascii>', ascii_values)

for tag in tags:
    print(tag)
