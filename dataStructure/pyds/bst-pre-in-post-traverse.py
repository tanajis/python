#=============================================================================================
#!/usr/bin/env python
#title           :bst-pre-in-post-traverse.py
#description     :Binary Search Tree PreOrder ,InOrder ,PostOrder traversals
#author          :Tanaji Sutar
#date            :2020-Mar-20
#python_version  :2.7/3
# #============================================================================================


####################################################
#Input list :[1,8,0,6,5,3,10,9,7,2,4]
#PRE ORDER:'5 2 1 0 4 3 8 7 6 10 9'
#IN ORDER:' 0 1 2 3 4 5 6 7 8 9 10'
#POST ORDER:'0 1 3 4 2 6 7 9 10 8 5'
#
#
#
#                   5
#                 /   \
#                /     \
#               2        8
#              / \      / \
#             1   4    7   10
#            /   /    /   / 
#           0   3    6   9
# 
#######################################################          

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self,dataset):
        
        dataset = sorted(dataset)
        tot_elemnets = len(dataset)
        self.root_element = self.AddData(dataset)
        self.PREORDER = str.strip(self.getPreOrder())
        self.INORDER = str.strip(self.getInOrder())
        self.POSTORDER = str.strip(self.getPostOrder())
        

    def AddData(self,dataset):

        if len(dataset) == 1:
            newNode = Node(dataset[0])
            return newNode
        else:
            tot_elemnets = len(dataset)
            root_element = dataset[int(tot_elemnets/2)]
            #print(dataset[int(tot_elemnets/2)])
            newNode = Node(root_element)
            left_data = dataset[:tot_elemnets/2]
            if left_data:
                #print('left')
                newNode.left = self.AddData(left_data)

            right_data = dataset[(tot_elemnets/2 +1):]
            if right_data:
                #print('right')
                newNode.right = self.AddData(right_data)
            return newNode

    def getTreeJson(self,node):
        treeJson = {}
        
        treeJson['root'] = str(node.data)
        if node.left:
            treeJson['left'] = self.getTreeJson(node.left)
        
        if node.right:
            treeJson['right'] = self.getTreeJson(node.right)
        
        return treeJson

    def getPreOrder(self,node=None):

        if node is None:
            node = self.root_element
        
        #root-->left-->right
        path = str(node.data) +' '

        if node.left:
            path = path + self.getPreOrder(node.left)
        
        if node.right:
            path = path + self.getPreOrder(node.right)
        
        return path

    def getInOrder(self,node=None):

        if node is None:
            node = self.root_element
        
        #left-->root-->right
        
        path = ''

        if node.left:
            path = path + self.getInOrder(node.left)
        
        path = path + ' ' + str(node.data)
        
        if node.right:
            path = path + self.getInOrder(node.right)
        
        return path

    def getPostOrder(self,node=None):

        if node is None:
            node = self.root_element
        
        #left-->right-->root
        
        path = ''

        if node.left:
            path = path + self.getPostOrder(node.left)
        
        if node.right:
            path = path + self.getPostOrder(node.right)

        path = path + ' ' + str(node.data)
        
        return path

if __name__ == "__main__":

    data = [1,8,0,6,5,3,10,9,7,2,4]

    bt = BinarySearchTree(data)
    
    #print(bt.getTreeJson(bt.root_element))

    print('PRE ORDER  :%r' % bt.PREORDER)
    print('IN ORDER   :%r' % bt.INORDER)
    print('POST ORDER :%r' % bt.POSTORDER)


    assert bt.PREORDER ==  '5 2 1 0 4 3 8 7 6 10 9'
    assert bt.INORDER ==   '0 1 2 3 4 5 6 7 8 9 10'
    assert bt.POSTORDER == '0 1 3 4 2 6 7 9 10 8 5'

