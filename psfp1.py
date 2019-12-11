items = [11, 13, 12, 14, 13, 15, 255]

# print(hex)
# print(hex(5))

# m = map(hex, items)  # functional programming, callable object
# m2 = map(str.upper, m)
# # print(m)
#
# for item in m2:
#     print(item)

m = map(ord, 'peter pan')
print(m)
print(list(m))