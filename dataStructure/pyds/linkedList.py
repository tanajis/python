#==============================================================================
#!/usr/bin/env python
#title           :linkedList.py
#description     :This is linked list implementation in python.
#author          :Tanaji Sutar
#date            :2019-Sep-22
#python_version  :2.7  
#Notes: Linked list methods -init,append,prepend ,search,remove,reverse
#==============================================================================

class Node:
    """
    This is node class for data structure of linked list.
    This is used internally by SinglyLinkedList class.
    This class implement basic init and repr method only
    """
    def __init__(self,data=None ,next=None):
        self.data=data
        self.next=next
    def __repr__(self):
        return self.data
    
class SinglyLinkedList():
    """
    This is SinglyLinkedList class which contains heads of list object.
    This is used by main program.
    """
    def __init__(self):
        """
        This method initialised list by creating head node
        """
        self.head=None

    def append(self,data):
        """
        This method append the data at the end of the list
        """
        if not self.head:
            #if head is None(empty) then assign data to head
            self.head=Node(data)
            return
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            #create new node and assign to next of last node
            curr.next=Node(data)
    
    def prepend(self,data):
        """
        This method add the data to the begining of the list
        """ 
        if not self.head:
            self.head=Node(data)
            return 
        else:
            old_start=self.head #detect start
            new_start=Node(data,old_start) #create new node with next pointing to old start
            self.head=new_start #assign head to new node
            

    def search(self,data):
        """
        This method accept data and search it in LL and return its index.
        """
        i=0
        curr=self.head
        if curr.next is None:
            if curr.data==data:
                print('data found in linked list at start only')
                return i
            else:
                print('No data found')
                return None
        else:
            while(curr.next):
                if curr.data==data:
                    print('data found in linked list at %i ' %i)
                    return i
                else:
                    curr=curr.next
                i=i+1
            if curr.data==data:
                print('data found in linked list at the end %i ' %(i))
                return i
            else:
                print('No data found in the Linked list')
                return None

    def remove2(self,data):
        ind=self.search(data)
        print('ind',ind)
        curr=self.head
        prev=curr
        if ind is not None:
            print('jjj')
            if self.head.next is None:
                self.head.data=None
                print('start')
                return

            for i in range(ind+1):
                print('i',i)
                if i==ind:
                    print('lll',curr.data)
                    next=curr.next
                    if curr==self.head:
                        self.head=next
                    prev.next=next 
                    print('removed successfully')
                    return
                prev=curr
                curr=curr.next


             


    def remove(self,data):
        """
        This method deletes the first occurance of the data if present in the list
        """
        #if only 1 node
        curr=self.head
        if curr.next is None:
            if curr.data==data:
                curr.data=None
                return
            else:
                print('data is not present in the linked list')
                return
        else:
            curr=self.head
            prev=None
            next=None
            while curr.next:
                if curr.data==data:
                    #key found
                    next=curr.next
                    prev.next=next
                    print('Data is deleted')
                    return
                prev=curr
                curr=curr.next
            print('Data not found in Linked list')




    def __repr__(self):
        """
        This method prints all the data in list format.
        When we call print of object of this class, this get executed.
        """
        nodes=[]
        curr=self.head
        while curr:
            nodes.append(repr(curr))
            curr=curr.next
        return '[' +', '.join(nodes) + ']'

if __name__ == "__main__":
    #initialise the linked list
    lst=SinglyLinkedList()

    #Append Data to list
    lst.append('a')
    
    #print whole list
    print(lst)

    lst.append('b')
    lst.append('c')
    print(lst)
    lst.prepend('d')
    print(lst)
    #print(lst.search('c'))
    print(lst)     
    lst.remove2('b')
    print(lst)
