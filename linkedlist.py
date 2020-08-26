from collections import deque
"""
deque uses an implementation of a linked list in which you can
access, insert, or remove elements from the beginning or end of a list
with constant O(1) performance. To populate the linked list, pass in an
iterable such as a string or list of objects
"""
deque(['jacob','matthew','bryan','mark'])

"""
Since a deque is a double-ended queue, it has the flexibility to
act as a queue or a stack
"""

"""
Queue Implementation: append elements to the right
"""
queue = deque()
queue.append('martha')
queue.append('susan')
queue.append('cate')
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

"""
Stack Implementation: append elements to the left
"""
queue = deque()
queue.appendleft('plate1')
queue.appendleft('plate2')
queue.appendleft('plate3')
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

