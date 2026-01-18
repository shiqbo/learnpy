from multiprocessing import Process, Queue

q = Queue(3)

q.put('Hi, John.')
q.put('Goodbye.')
q.put('See u again.')

#print(q.qsize())

print(q.empty())
print(q.full())

print(q.get())
print(q.get())

print(q.empty())
print(q.full())
