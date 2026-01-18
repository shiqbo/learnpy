import re

result = re.match(r'w\w+', 'hello world')
if result:
    print(result.group())
else:
    print('f')

###
result = re.search(r'w\w+', 'hello world')
if result:
    print(result.group())
else:
    print('f')

result = re.search(r'w\w+', 'hello world world world')
if result:
    print(result.group())
else:
    print('f')

result = re.search(r'w\w+', 'hello')
if result:
    print(result.group())
else:
    print('f')

###
result = re.findall(r'w\w+', 'hello')
print(result)

result = re.findall(r'w\w+', 'hello world')
print(result)

result = re.findall(r'w\w+', 'hello world world world')
print(result)

###
string = 'hello world world world'
result = re.sub('hello', 'world', string)
print(result)
result = re.sub('world', 'hello', string, count=2)
print(result)
result = re.sub('^w.*d$', 'hello', string, count=2)
print(result)

###
string = '1234567abc'
res = re.match('\d*', string)
print(res.group())
res = re.match('\d+', string)
print(res.group())
res = re.match('\d{2,5}', string)
print(res.group())


res = re.match('\d*?', string)
print(res.group())
res = re.match('\d+?', string)
print(res.group())
res = re.match('\d{2,5}?', string)
print(res.group())
