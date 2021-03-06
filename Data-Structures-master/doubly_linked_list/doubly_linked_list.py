class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.next:
            self.next.prev = self.prev  

        if self.prev:
            self.prev.next = self.next

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

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):

        val = self.head.value
        self.delete(self.head)

        return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):

        new_node = ListNode(value)
        self.length += 1

        if not self.tail and not self.head:
            self.head = new_node

            self.tail = new_node

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):

        val = self.tail.value


        self.delete(self.tail)
        return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):

        val = node.value

        if node is self.tail:
            self.remove_from_tail()
            
        else:
            node.delete()
            self.length -= 1

        self.add_to_head(val)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):

        value = node.value

        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):

        self.length -= 1

        if self.head == node:
            self.head = node.next
            node.delete()

        if self.tail == node:
            self.tail = node.prev
            node.delete()

        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):

        current = self.head.next
        the_max = self.head.value

        while current:

            if current.value > the_max:
                the_max = current.value
            current = current.next

        return the_max