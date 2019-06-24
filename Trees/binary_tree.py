class Node:
    def __init__(self, value):
        if value:
            self.value = value
        else:
            self.value = None
        
        self.left = None
        self.right = None

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node
    
    def has_left_child(self):
        return not self.left == None
    
    def has_right_child(self):
        return not self.right == None

class Tree:
    def __init__(self, value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root    