from typing import TypeVar

T = TypeVar('T')

class Node:
    def __init__(self, data: T):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: T):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()

# Example usage
llist = LinkedList()
llist.append(1)
llist.append("hello")
llist.append(3.14)
llist.print_list()
