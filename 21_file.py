'''
f = open('tmp', 'r', encoding='utf-8')
f.close()


with open('tmp' , 'r', encoding='utf-8') as f:
    content = f.read(30)
    content2 = f.readline()
    content3 = f.readlines()

print(content)
print(content2)
for line in content3:
    print(line)

print(f.closed)


with open('tmp1' , 'w', encoding='utf-8') as f:
    f.write('empty file')


with open('tmp2' , 'a+', encoding='utf-8') as f:
    f.write('hello world')
    print(f.tell())
    print(f.read())
    f.seek(0)
    print(f.read())


with open('img.png' , 'rb') as f:
    f.read()
'''


