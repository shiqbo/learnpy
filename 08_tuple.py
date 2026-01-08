tup1 = (1)
print(tup1, type(tup1))
tup2 = (1,)
print(tup2, type(tup2))

t = ('Sun',' Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
print(t, type(t))

# index and slice
print(t[1])
print(t[-3])
print(t[2:6:2])
print(t[-1:-5:-1])

print(t.index('Thu'))

# member
print('Thu' in t)
print('Thu' not in t)

# count
print(t.count('Thu'))
print(t.count('p'))
