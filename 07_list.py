l = ['a', 'b', 3, 5, 7, 'c']
print(l)
print(type(l))

# index
print(l[0])
print(l[3])

# slice
print(l[:4])
print(l[::])
print(l[::-1])
print(l[::-2])

# change item
l[2] = 4
print(l)

# nest
l = [[1,2,3], 'a', ['b', 'c']]
print(l)
print(l[0][0])

# builtin function
l.append(['d', 'e'])
print(l)

l. extend('gh')
print(l)

l.insert(1, 4)
print(l)

print(l.index('h'))

print(l.count('h'))

l.remove('h')
print(l)

l.reverse()
print(l)

