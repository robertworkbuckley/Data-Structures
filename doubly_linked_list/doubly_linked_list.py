"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
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
        # create instance of ListNode with value
        # node = ListNode(value)
        if not self.head:
            node = ListNode(value)
            self.head = node
            self.tail = node
            self.length = 1
        elif self.head == self.tail:
            old_head = self.head
            # new_node = ListNode(value, prev=None, next=old_head)
            # old_head.prev = new_node

            self.head = ListNode(value, prev=None, next=old_head)
            old_head.prev = self.head
            self.tail = old_head
            self.length += 1
        else:
            old_head = self.head
            self.head = ListNode(value, prev=None, next=self.head)
            old_head.prev = self.head
            self.length += 1


        
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
        self.head = self.head.next
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
            #old head being replaced:
            old_head = self.head

            #new tail:
            new_tail = self.tail.prev
            self.tail = new_tail
            self.tail.next = None

            #update old head pointer:
            old_head.prev = node

            #make new head:
            node.prev, node.next = None, old_head
            self.head = node
        else:
            #update pointers of nodes from both side of 'moving node' to now point at 
            #each other
            node.prev.next, node.next.prev = node.next, node.prev

            #updates pointers of old head being replaced:
            old_head = self.head
            old_head.prev = node

            #node being moved; updates pointers; assigns as new head
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
            #old tail being replaced:
            old_tail = self.tail

            #new head:
            new_head = self.head.next
            self.head = new_head
            self.head.prev = None

            #update old tail pointer:
            old_tail.next = node

            #make a new tail:
            node.prev, node.next = old_tail, None
            self.tail = node
        else:
            #update pointers of nodes from both side of 'moving node' to now point at 
            #each other
            node.prev.next, node.next.prev = node.next, node.prev

            #update pointers of old tail being replaced:
            old_tail = self.tail
            old_tail.next = node

            #node being moved; updates pointers; assigns as new head
            node.prev, node.next = old_tail, None
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass