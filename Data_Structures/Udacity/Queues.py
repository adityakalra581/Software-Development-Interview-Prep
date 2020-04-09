## Queue as a List:
## In general queue is First in First out.


from collections import deque
## deque : double sided queue

## Reference : https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues


## Head is the First element.
## Tail is the last element.
## peek is just seeing the top of the queue
## Enqueue : Inserting element into the queue
## Dequeue : Deleting the element from the queue.

class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]     

    def dequeue(self):
        return self.storage.pop(0)
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())
