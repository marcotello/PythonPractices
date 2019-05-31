# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

def to_list(linked_list, lst):
        node = linked_list.head
        while node:
            lst.append(node.value)
            node = node.next

        return lst

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    temp_list = []
    # merged_list = None

    temp_list = to_list(list1, temp_list)
    temp_list = to_list(list2, temp_list)

    temp_list.sort()
    
    llist = LinkedList(Node(temp_list[0]))
    index = 1

    while index < len(temp_list):
        llist.append(temp_list[index])

    return llist
    

class NestedLinkedList(LinkedList):
    def flatten(self):
        # TODO: Implement this method to flatten the linked list in ascending sorted order.
    



# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

nested_linked_list = NestedLinkedList(Node(linked_list))

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list.append(Node(second_linked_list))

merge(linked_list, second_linked_list)