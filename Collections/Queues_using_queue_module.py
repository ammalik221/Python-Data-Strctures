"""
Queues Implementation in Python 3.0 using deque module.

For implementations from scratch, check out the other files in this repository.
"""

from collections import deque

# test cases
# make a deque
q = deque()

# add elements
q.append(20)
q.append(30)
q.append(40)

# output is - 10 20 30 40
print(q)

# remove elements from queue
# output is 10 and 20 respectively
print(q.popleft())
print(q.popleft())
