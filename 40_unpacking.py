t = (1, 2, 3)
a, b, c = t
print(a, b, c)

l = [1, 2, 3, 4]
a, b, c, d = l
print(a, b, c, d)

s = [1, (2, 3), 4]
a, b, c = s
print(a, b, c)

x = [1, 2, 3]
a, *b = x
print(a, b)

y = [1, 2, 3, 4, 5]
a, *b, c = y
print(a, b, c)

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, ':', v)