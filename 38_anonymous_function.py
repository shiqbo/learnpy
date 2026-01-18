def add(a, b):
    return a + b
print(add(3, 4))


add2 = lambda a, b: a + b
print(add2(3, 4))


l = [
    {'name': 'John', 'age': 25, 'score': 88},
    {'name': 'Shelley', 'age': 25, 'score': 77},
    {'name': 'Bob', 'age': 25, 'score': 99},
    {'name': 'Anna', 'age': 25, 'score': 66}
]
r = sorted(l, key=lambda x: x['score'], reverse=True)
print(r)