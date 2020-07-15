def reverse_ll(ll):
    """
    Recieve a LinkedList as an input and returns a reversed order LL

    Steps:
    1. Each node needs to point at the prev_node
    2. Head and tail pointers need to be flipped

    Case:
    1. If the ll is empty return the orignal that is passed in

    reverse_(ll)
    """
    # if LL is empty, return LL
    if ll.head is None:
        return ll

    # If LL has one node
    if ll.head is ll.tail:
        return ll

    # if LL has two or more nodes
    current = ll.head
    previous = None
    next_node = None
    while current is not None:
        # store a pointer to the current next value
        next_node = current.get_next()

        # switch current's next pointer to the previous
        current.set_next(previous)

        # increment logic
        previous = current
        current = next_node

    ll.head, ll.tail = ll.tail, ll.head