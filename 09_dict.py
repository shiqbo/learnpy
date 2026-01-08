d = {'a': 'Sun', 'b': 'Mon', 'c': 'Wed', 'd': 'Thu', 'e': 'Fri', 'f': 'Sat'}
print(d, type(d))

print(d['f'])

print(d.get('f', None))
print(d.get('h', None))

d['h'] = 'Week'
print(d)
d['h'] = 'Weekend'
print(d)

print(d.keys())
print(d.values())
print(d.items())

tmp = d.pop('h')
print(d)
print(tmp)

d.clear()
print(d)

del d
