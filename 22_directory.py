import os

#os.rename('tmp', '../img')
#os.remove('../img')

if not os.path.exists('./tmp'):
    os.mkdir('./tmp')
print(os.getcwd())
print(os.listdir())
print(os.path.isfile('./tmp'))
print(os.path.isdir('./tmp'))
os.rmdir('./tmp')
