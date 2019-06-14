class Queue: 

    def __init__(self, initial_size = 10): 

        self.arr = [0 for _ in range(initial_size)] 
        self.next_index = 0 
        self.front_index = -1 
        self.queue_size = 0 

    def enqueue(self, value):
        # enqueue new element
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1) % len(self.arr)
        if self.front_index == -1:
            self.front_index = 0
    
    # TODO: Add the dequeue method
    def dequeue(self):
        if self.is_empty():
            self.next_index = 0 
            self.front_index = -1 
            self.queue_size = 0 
            return None
        
        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1) % len(self.arr) 
        self.queue_size -= 1
        return value

    
    # TODO: Add the size method
    def size(self):
        return self.queue_size
    
    # TODO: Add the is_empty method
    def is_empty(self):
        return self.queue_size == 0

    # TODO: Add the front method
    def front(self):
        if self.is_empty():
            return None
        else:
            return self.arr[self.front_index]
    
    def _handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]

        index = 0

        # copy all elements from front of queue (front-index) until end
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1

        # case: when front-index is ahead of next index
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1

        # reset pointers
        self.front_index = 0
        self.next_index = index

    