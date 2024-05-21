from data_structures.linked_list import LinkedList


class StackLinkedList:
    def __init__(self):
        self.llist = LinkedList()

    def push(self, data):
        self.llist.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        current_node = self.llist.head
        prev_node = None
        while current_node.next:
            prev_node = current_node
            current_node = current_node.next
        if prev_node:
            prev_node.next = None
        else:
            self.llist.head = None
        return current_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        current_node = self.llist.head
        while current_node.next:
            current_node = current_node.next
        return current_node.data

    def is_empty(self):
        return self.llist.head is None

# Example usage
stack = StackLinkedList()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack elements:")
while not stack.is_empty():
    print(stack.pop())

# Output:
# 3
# 2
# 1
