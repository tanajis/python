# This problem was asked by Google.
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.
# For example, given the following Node class
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
#=============================================================================================
#!/usr/bin/env python
#title           :problem3.py
#description     :Daily coding problem
#author          :Tanaji Sutar
#date            :2020-Jan-19
#python_version  :2.7/3  
#============================================================================================


import json


class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right


    def serialize(self):
        """
        create string representation of given tree
        """
        if self is None:
            return None
        else:
            dict={}
            dict['data']=self.data
            if self.left:
                dict['left']=self.left.serialize()

            if self.right:
                dict['right']=self.right.serialize()

            #convert dictionary to string
            #return json.dumps(dict)
            return dict
    
    def is_json(self,myjson):
        try:
            json_object = json.loads(str(myjson))
        except ValueError as e:
            return False
        return True

    def deserialize(str1):
        """
        create tree as per string provided
        """
        #print('call',str1)
        dict=str1
        #dict=json.dumps(str1)
        #print(dict)

        if 'data' in dict.keys():
            
            root=Node(dict['data'])
            #print('Node:',dict['data'])
            
            if 'left' in dict.keys():
                root.left=Node.deserialize(dict['left'])
            
            if 'right' in dict.keys():
                root.right=Node.deserialize(dict['right'])
                
            return root






if __name__ == "__main__":
    root=Node('a')
    b=Node('b')
    c=Node('c')
    d=Node('d')
    e=Node('e')

    root.left=b
    root.right=e
    b.left=c
    b.right=d
    
    print('Tree to String')
    ser=root.serialize()
    print(ser)

    print('String to tree')
    root2=Node.deserialize(ser)
    print('root',root2.data)
    print('left',root2.left.data)
    print('right',root2.right.data)
    print('left.left',root2.left.left.data)
    print('left.right',root2.left.right.data)

    #Given test case
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert Node.deserialize(node.serialize()).left.left.data == 'left.left'



"""
Our Tree is as below:

         a
        / \
       b   e
       /\
      c  d

Serialise will print below
    {'data': 'a', 
 'left': {'data': 'b', 
          'left': {'data': 'c'}, 
		  'right': {'data': 'd'}
		  }, 
 'right': {'data': 'e'}
 }

 """
        
