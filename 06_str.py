a = 'hello'
b = 'world'

# concatenate
c = a + b
print(c)

# repeat
d = a * 3
print(d)

# member
print('o' in a)
print('a' not in a)

# index
print(a[0])
print(a[2])
print(a[-1])
print(a[-4])

# slice
print(a[1:-1])
print(a[1:4])
print(a[:])
print(a[::])
print(a[0:4:2])
print(a[::-2])

# escape
print('\t\tabc')
print('ab\nc')
print('C:\\tools')
print(r'C:\tools')
print('it\'s right')
print("it's right")

# format
name = 'john'
age = 50
print(f'{name} is {age} years old')

i = 2
j = 3
print(f'{i} x {j} = {i*j}')
print(f"{i}'s type is {type(i)}")

n = 20260108
print(f'my id is {n:20}')
print(f'my id is {n:020}')
print(f'my id is {n:>20}')
print(f'my id is {n:0>20}')
print(f'my id is {n:^20}')
print(f'my id is {n:0^20}')
print(f'my id is {n:<20}')
print(f'my id is {n:0<20}')

m = 3.1415926
print(f'PI is {m:.2f}')
print(f'PI is {m:.10f}')

# builtin function
z = 'hello python3'

print(z.find('on'))
print(z.index('on'))
print(z.count('o'))

x = z.replace('python3', 'world')
print(z)
print(x)

c = z.split()
print(z)
print(c)

v = z.split('o')
print(z)
print(v)

b = z.split('o', 1)
print(z)
print(b)


t = '   hello   '
print(t)
print(t.strip())
print(t.rstrip())
print(t.lstrip())

u = 'xxxxhelloxxxx'
print(u)
print(u.strip('x'))

p = 'Hello'
print(p)
print(p.upper())
print(p.lower())


print(p.startswith('h'))
print(p.startswith('H'))

print(p.endswith('o'))
print(p.endswith('O'))

r = 'hello'
print(r.islower())
print(r.isupper())

# encode and decode
e = 'hello'
f = e.encode()
print(e)
print(f)
g = f.decode()
print(g)
