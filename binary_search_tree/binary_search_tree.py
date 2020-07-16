"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
               self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
               self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: target is less than self.value 
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop construct

        if not self.right:
            return self.value
        else:
            return self.right.get_max()

        # value = self.value
        # current_node = self.right
        # while current_node is not None:
        #     value = current_node.value
        #     current_node = current_node.right

        # return value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
       # recursive solution
        if self.value:
            fn(self.value)
            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)

        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if current nod is None
        # we know we've reache the end of a recurion

        # (base case) we want to return
        if self is None:
            return
        if self.left is not None:
            self.left.in_order_print()

        # visit the node by print its value
        print(self.value)

        if self.right is not None:
            self.right.in_order_print()



        pt_list = []
        for_each(pt_list.append)
        for i in pt_list.sort():
            print(1)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # Use a queue to form a "line"
        # for the nodes to "get in"

        # start by placing the root in the queue
        
        #need a while loop to iterate
        # what are we checking in the whiel statement?
        # while length of queue is greater than 0
            # dequeue item from front of queue
            # print that item

            # place current items's left node in queue
            # place current item's right nod in queue

        # place left node in queue if not None

        # place right node in queue if not None

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # initialize an empty stack
        # push the root node onto the stack

        # need a while loop to manage the iteration
        # wif stack is not empty enter the while loop
            # pop top item off the stack
            # print that item's value

            # if there is a left subtree
                # push left item onto the stack
            
            # if there is a right subtree
                # push right item onto the stack
                



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bs = BSTNode(3)
bs.insert(5)
bs.insert(2)
bs.insert(89)
bs.insert(22)
