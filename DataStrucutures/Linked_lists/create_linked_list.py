class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    
    if len(input_list) != 0:
        head = Node(input_list[0])
        index = 1
        current = head
        while index < len(input_list):
            current.next = Node(input_list[index])
            current = current.next
            index += 1

    return head

def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


mylist = [3, 4, 6, 8, 1, 2, 7, 33]
head = create_linked_list(mylist)
print_linked_list(head)