class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)


def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next

print_linked_list(head)

'''
print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)
'''