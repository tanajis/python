###############################################################################
# problem 6
# Good morning! Here's your coding interview problem for today.
# This problem was asked by Google.
# An XOR linked list is a more memory efficient doubly linked list.
#  Instead of each node holding next and prev fields, it holds a field 
# named both, which is an XOR of the next node and the previous node. 
# Implement an XOR linked list; it has an add(element) which adds the element to the end, 
# and a get(index) which returns the node at index
###############################################################################

#XOR Doubly linked list 

# a-->b--->c--d
#list is empty. insert a .npx will be XOR(None,None )= None
#insert b. npx of b will be XOR(npx(a),None)
#Python id() function returns the "identity" of the object. 
#The identity of an object is an integer, which is guaranteed to be unique and 
# constant for this object

class Node:
    def __init__(self, data):
        self.data = data
        self.nexprev = id(data)

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.dict = {}
        self.dict[data] = id(new_node)


    def add(self, data):

        #Create new Node
        newNode = Node(data)

        #update last elements pointer
        self.tail.nexprev =self.tail.nexprev ^ id(newNode.data)
        
        #update new element pointing prev element
        newNode.nexprev = id(self.tail.data)
        
        #set tail pointer to new Node
        self.tail = newNode

        self.dict[data] = id(newNode)

    
    def printLinkList(self):

        prev = None
        curr = self.head
        next = curr.nexprev

        print(prev,next,curr)
        """
        while(1):
            print(curr.data)
            prev = curr
            next = curr.nexprev
            if curr == self.tail:
                break
        """
    """
    def get(self, index):
        prev_node_address = 0
        result_node = self.head
        for i in range(index):
            next_node_address = prev_node_address ^ result_node.both
            prev_node_address = id(result_node.data)
            result_node = id_map[next_node_address]
        return result_node.data
    """

llist = LinkedList('a')
llist.add('b')
llist.add('c')
llist.add('e')

llist.printLinkList()

print(llist.dict)

"""
assert llist.get(0) == "c"
assert llist.get(1) == "d"
assert llist.get(2) == "e"
assert llist.get(3) == "a"
"""
