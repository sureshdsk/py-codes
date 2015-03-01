# Tutorial: http://www.idiotinside.com/2015/03/01/python-lists-as-fifo-lifo-queues-using-deque-collections

stack = ["a", "b", "c"]

# add an element to the end of the list
stack.append("e")
stack.append("f")
print stack

# pop operation
stack.pop()
print stack

# pop operation
stack.pop()
print stack

# push operation
stack.append("d")
print stack