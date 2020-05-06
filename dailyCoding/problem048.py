Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g


##############################################


PREORDER = [a, b, d, e, c, f, g]
INORDER = [d, b, e, a, f, c, g]


#--------------------------------------

step 1 : pick element from preorder,create node using it and mark it processed in preorder.
step 2 : find that element in in order.
step 3: recursively pass all the element to left side to create tree and point it as root.left
step 4: recursively pass all the element to right side to create tree and point it as root.right
step 5: if only one element ,create node, mark it processed in preorder and return node.




        
        
        





