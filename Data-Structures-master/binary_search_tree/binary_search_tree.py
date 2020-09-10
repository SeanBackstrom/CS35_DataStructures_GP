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
        # if single element :
        if self.contains(value) == True:
            new_node = BSTNode(value)
            self.right = new_node
        # compare target.value to node.value
        # if value > node.value
        if value > self.value:
            # go right
            # if node.right is None:
            if self.right is None:
            # create new node there
                new_node = BSTNode(value)
                self.right = new_node

            else:
                # do same thing (aka recurse)
                # insert value into node.right
                self.right.insert(value)

        # Else if value < node.value:
        if value < self.value:
            # go left
            # if node.left is None:
            if self.left is None:
                # create the node 
                self.left = BSTNode(value)
                
            else:
                # Do the same thing
                #   comapre , go left rght
                self.left.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target value to node.value
        #if target == node.value:
        if target == self.value:
            return True
        if target > self.value:
            # go right
            if self.right is None:
                # We didnt find it
                return False
            else:
                #do the same thing
                return self.right.contains(target)
        if target < self.value:
            #go left
            if self.left is None:
                return False
            else:
                # Do the same thing
                #compare, go left or right
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #The node with the max val is the right most node

        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
        


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        
        #left one
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)

        if self.right is not None:
           
            self.right.for_each(fn)

        if self.right and self.left is None:
            return
        
        return 
            
        
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

#bst.bft_print()
#bst.dft_print()

print("elegant methods")
print("pre order")
#bst.pre_order_dft()
print("in order")
#bst.in_order_dft()
print("post order")
#bst.post_order_dft()  
print(bst.get_max())
