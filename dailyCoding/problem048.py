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


step 1: initialise ind = 1
step 2: if ind is 1 then pick PREORDER[ind] as root 
          set parent to  PREORDER[ind]
          increament ind
        else
          pick new as PREORDER[ind] perform step 3 and 4
step 3: If position of new less than position of parent in INORDER then
          if left of parent is empty
            set new element as left of parent
            set parent to parent.left
          else
            parent = parent.left
        
        ELSE
        set new element as right of parent
        set parent to parent.right
step 4: increament ind and go to step 2
        
        
        
        
        





