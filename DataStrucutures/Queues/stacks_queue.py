# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        # Code here
        self.num_elements = 0
        self.stack = Stack()
        
    def size(self):
         # Code here
         return self.num_elements
        
    def enqueue(self,item):
        # Code here
        self.stack.push(item)
        self.num_elements += 1
        
    def dequeue(self):
        # Code here
        temp_stack = Stack()
        for i in range(self.num_elements):
            temp_stack.push(self.stack.pop())
        
        value = temp_stack.pop()
        self.num_elements -= 1
        
        for i in range(self.num_elements):
            self.stack.push(temp_stack.pop())
        
        return value


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

