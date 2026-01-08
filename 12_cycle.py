n = 1
m = 0
while n <= 100:
    m +=n
    n += 1
print(m)


i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f'{j} x {i} = {i*j}', end='\t')
        j += 1
    print()
    i += 1
print()


c = 0
for i in range(1, 101):
    c += i
print(c)


for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j} x {i} = {i*j}', end='\t')
    print()
print()


l = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    l += i
print(l)


k = 0
for i in range(1, 101):
    if i % 2 == 0:
        break
    k += i
print(k)
