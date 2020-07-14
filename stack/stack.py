import sys
sys.path.append(".")

from singly_linked_list.singly_linked_list import Node, LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# 1.
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         return self.storage.pop(-1)


# 2.
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        count = 0
        current_node = self.storage.head

        while current_node is not None:
            count = count + 1

            current_node = current_node.next_node
        return count

    def push(self, value):
        if not self.storage.head:
            self.storage.head = Node(value)
            self.storage.tail = Node(value)
        else:
            self.storage.head = Node(value, self.storage.head)

    def pop(self):
        return self.storage.remove_head()
