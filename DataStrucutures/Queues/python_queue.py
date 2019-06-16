class Queue:
    def __init__(self):
        # TODO: Initialize the Queue
        self.lst = list()
    
    def size(self):
        # TODO: Check the size of the Queue
        return len(self.lst)
    
    def enqueue(self, item):
        # TODO: Enter item into Queue
        self.lst.append(item)

    def dequeue(self):
        # TODO: Remove item from the Queue
        if(len(self.lst) > 0):
            return self.lst.pop(0)
        else:
            return None

# Setup
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")