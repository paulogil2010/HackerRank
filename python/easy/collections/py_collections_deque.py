"""
Perform append, pop, popleft and appendleft methods on an empty deque D.

"""


from collections import deque

num_operations = int(input())

d = deque()
operations = []

for i in range(num_operations):
    operations.append(input())

for operation in operations:
    op = operation.split(' ')
    if 'append' in op and not 'appendleft' == op[0] :
        d.append(op[-1])
    if 'appendleft' in op:
        d.appendleft(op[-1])
    if 'clear' in op:
        d.clear()
    if 'extendleft' in op:
        d.extendleft(op[-1])
    if 'count' in op:
        d.count(op[-1])
    if 'pop' in op:
        d.pop()
    if 'popleft' in op:
        d.popleft()
    if 'extend' in op:
        d.extend(op[-1])
    if 'remove' in op:
        d.remove(op[-1])
    if 'reverse' in op:
        d.reverse()
    if 'rotate' in op:
        d.rotate(op[-1])

for i in d:
    print(i, end=" ")
