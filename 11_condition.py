n = 6

print(3 > 2)
print(3 < 2)
print(3 != 2)
print(3 == 2)

print(3 > 2 and n == 8)
print(3 < 2 or n == 8)
print(not 3 > 2)

if not isinstance(n, int):
    print('invalid')
elif n % 2 == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')
print('outside')
