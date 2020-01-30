#=============================================================================================
#!/usr/bin/env python
#title           :bst.py
#description     :Binary Search Tree Python implementation.
#author          :Tanaji Sutar
#date            :2020-Jan-30
#python_version  :2.7/3
#Methods         : Create BST,Binary search, Delete Key, print BST
#============================================================================================


class Node():

    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
    

    def insert(self,data):
        #check if self is NULL or not
        if self.data:
            #Self is not NULL

            if data <self.data:
                #if data is smaller , check at left side
                if self.left is None:
                    #if left is empty/None assign to left
                    self.left=Node(data)
                else:
                    #if left has node.call insert for that node recursively
                    self.left.insert(data)

            elif data>self.data:
                #data is larger that current. Check at right
                if self.right is None:
                    #If right is Empty assign new Node to it.
                    self.right=Node(data)
                else:
                    #If right is not empty, Call insert for right node recursively.
                    self.right.insert(data)
            
            else:
                #Self is NULL. Assign value to it directly
                self.val=data


    def minValueNode(self):
        """
        This function is needed for function : delete(self,data)
        Given a non-empty binary search tree, it return the node with minimum key value found
        in that tree.Note that the entire tree does not need to be searched 
        """
        current_node=self
        #Min will be found at left only.Go left till we dont get NULL
        while (current_node.left is not None):
            current_node=current_node.left
        
        #After getting left most ,return it
        return current_node

    def delete(self,key):

        #Base case
        if self is None:
            print('Given root is Empty.Nothing to delete.')
            return self
        
        #Check if key is at left side,call for left recursively
        if key <self.data:
            self.left=self.left.delete(key)
        
        #Check if key is at right side,call for right recursively
        if key >self.data:
            self.right=self.right.delete(key)
        
        #if key matches current node
        else:
            #Case 1: If No child or only one child (either left or right)--> return it as Node
    
            if self.left is None:
                temp=self.right
                return temp

            else:
                self.right is None
                temp=self.left
                return temp

            #Case 2: If tow children found-->Get the inorder successor.
            # (smallest in the right subtree will be new root)

            #get smallest in the right
            temp=self.right.minValueNode()

            #Replace currents value with temp's value
            self.data=temp.data

            #Delete inorder successor 
            self.right=self.right.delete(temp.key)

        return self

    def printTree(self):
        #check if left exist.If exist, print left first
        if self.left:
            #if Exists, call printTree recursively
            self.left.printTree()

        #Now print self data
        print(self.data,end=' ')

        #check if right exist.If exist, print right.
        if self.right:
            self.right.printTree()


    def binarySearch(self,key):

        #If key is less than data, check at left
        if key<self.data:
            if self.left is None:
                #left is empty, key not found, return NULL
                print('Key %r  not found in binary tree' %key)
                return None
            
            #if left is not NULL,check at left recursively
            return self.left.binarySearch(key)

        #If key is greater than data, check at right
        if key>self.data:
            if self.right is None:
                #right is empty, key not found, return NULL
                print('Key %r not found in binary tree' %key)
                return None

            #if right is not NULL,check at right recursively.
            return self.right.binarySearch(key)
            
        #key equals to self.data
        else:
            print('Key %r Found!!' %key)


if __name__ == "__main__":
    
    #create Binary tree .myby will be the root node.
    mybt=Node(12)
    datalist=[12,6,14,3,7,14]
    for i in datalist:
        mybt.insert(i)

    print('---Binary Tree------------------------------------------')    
    mybt.printTree()
    print('\n------------------------------------------------------')
    mybt.binarySearch(6)
    mybt.binarySearch(3)
    mybt.binarySearch(14)
    mybt.binarySearch(100)

    min_value=mybt.minValueNode().data
    print(min_value)

    mybt.delete(7)

    mybt.printTree()


#============================================================================================
