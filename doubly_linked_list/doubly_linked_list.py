"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):

        new_node = ListNode(value)
        self.length += 1
        # if no head exists, new node created will become head and tail
        if not self.head:
            self.head = node
            self.tail = node
        # new node will point to old head, with old head pointing to new node that
        #is now the new head
        else:
            new_node.next = self.head
            self.head.prev =new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if not self.head:
            return "Error: DDL is currently empty."

        if not self.head.next:
            head = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return head.value

        value = self.head.value
        self.delete(self.head)
        self.length -= 1
        return value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        if not self.tail:
            node = ListNode(value)
            self.head = node
            self.tail = node
            self.length += 1
        else:
            old_tail = self.tail
            new_tail = ListNode(value, old_tail)
            self.tail = new_tail
            old_tail.next = new_tail
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if not self.tail:
            return "Error: DDL empty. Tail does not exist."
        if self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length = 0
            return value
        else:
            value = self.tail.value
            new_tail = self.tail.prev
            new_tail.next = None
            self.tail = new_tail
            self.length -= 1
            return value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if self.head == self.tail:
            return "Error: Only one nodes exists in current list."
        elif node == self.tail:
            # old head being replaced:
            old_head = self.head

            # new tail:
            new_tail = self.tail.prev
            self.tail = new_tail
            self.tail.next = None

            # update old head pointer:
            old_head.prev = node

            # make new head:
            node.prev, node.next = None, old_head
            self.head = node
        else:
            # update pointers of nodes from both side of 'moving node' to now point at
            # each other
            node.prev.next, node.next.prev = node.next, node.prev

            # updates pointers of old head being replaced:
            old_head = self.head
            old_head.prev = node

            # node being moved; updates pointers; assigns as new head
            node.prev, node.next = None, old_head
            self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if self.head == self.tail:
            return "Error: Only one node exists in list."
        elif node == self.head:
            # old tail being replaced:
            old_tail = self.tail

            # new head:
            new_head = self.head.next
            self.head = new_head
            self.head.prev = None

            # update old tail pointer:
            old_tail.next = node

            # make a new tail:
            node.prev, node.next = old_tail, None
            self.tail = node
        else:
            # update pointers of nodes from both side of 'moving node' to now point at
            # each other
            node.prev.next, node.next.prev = node.next, node.prev

            # update pointers of old tail being replaced:
            old_tail = self.tail
            old_tail.next = node

            # node being moved; updates pointers; assigns as new head
            node.prev, node.next = old_tail, None
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if len(self) == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif len(self) == 2:
            if node == self.head:
                new_head = self.tail
                # new_head.prev = None
                new_head.next, new_head.prev = None, None
                self.head = new_head
                self.tail = new_head
            elif node == self.tail:
                new_tail = self.head
                new_tail.next = None
                self.tail = new_tail
                self.head = new_tail
            self.length -= 1

        else:
            if node == self.head:
                new_head = self.head.next
                new_head.prev = None
                self.head = new_head
            elif node == self.tail:
                new_tail = self.tail.prev
                new_tail.next = None
                self.tail = new_tail
            else:
                # change pointers of nodes from both sides of the node being deleted, to now
                # point at each other, removing all reference of deleted node.
                node.prev.next, node.next.prev = node.next, node.prev
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current_node = self.head
        values = []

        while current_node is not None:
            values.append(current_node.value)

            current_node = current_node.next
        return max(values)


dl = DoublyLinkedList()
dl.add_to_head(9)
dl.add_to_head(18)
dl.add_to_head(3)
dl.add_to_head(7)