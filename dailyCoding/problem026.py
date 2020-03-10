
#=============================================================================================
#!/usr/bin/env python
#title           :problem026.py
#description     :DailyCoding #026   Medium
#author          :Tanaji Sutar
#date            :2020-Mar-10
#python_version  :2.7/3
#============================================================================================

# # This problem was asked by Google.
# # Given a singly linked list and an integer k, 
# # remove the kth last element from the list. 
# # k is guaranteed to be smaller than the length of the list.
# # The list is very long, so making more than one pass is prohibitively expensive.
# # Do this in constant space and in one pass.

# --my approach-------
#step 1:take two pointers p1 and p2. p1 will point to head and p2 keep as empty
#step 2:until we reach at the end of list perform below 3,4,5 steps
#step 3:move p1 to next
#step 4:if p1 is at nth node, set p2 at the starting node
#step 5:if p1 is at end, p2 will be at the last nth position from end,delete it
#end



class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
    
    def insert(self,data):
        curr = self
        #Go to the end

        while(curr.next):
            curr = curr.next
        
        #Create new node
        node = Node(data)
        
        #set new node at the end
        curr.next = node

    
    def printList(self):
        curr = self
        while(curr):
            print(curr.data,'--> ',end='')
            curr = curr.next

    def deletelastNthNode(self,n):
        curr = self
        p2  =None
        i = 1
        while(curr.next):
            curr = curr.next
            i += 1

            if p2:
                prev = p2
                p2 = p2.next
            if i == n:
                p2 = self
        
        #set prev of nth element pointing to next elemenmt from p2
        prev.next = p2.next

        #delete p2
        del p2
        print('Deleted last {} number node successfully'.format(n))


if __name__ == "__main__":
    
    mylinkedlist = Node('a')
    mylinkedlist.insert('b')
    mylinkedlist.insert('c')
    mylinkedlist.insert('d')
    mylinkedlist.insert('e')
    mylinkedlist.insert('f')
    mylinkedlist.insert('g')
    mylinkedlist.insert('h')
    
    mylinkedlist.printList()

    #Now delete 3rd last node
    # f should be deleted
    mylinkedlist.deletelastNthNode(3)

    mylinkedlist.printList()


