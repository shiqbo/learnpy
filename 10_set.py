s = {'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'}
print(s, type(s))

s = {'Sun', 'Sun', 'Sun', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'}
print(s, type(s))

print(type({}))
print(type(set()))

s.add(13)
print(s)

s.update('abc')
print(s)

s.remove('a')
print(s)

s.discard('c')
print(s)
s.discard(100)
print(s)

s.clear()
print(s)


s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.intersection(s2))
print(s1.union(s2))

l = [1,2,3,3,4,5,5,6,6,6,7]
print(list(set(l)))
