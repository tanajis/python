
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).



Solution:
  
  
  step 1:if leafnode is return int value
  step 2:if internal node push to stack
  step 3: leftval = calculate(left)
          rightval = calculate(right)
          return leftVal + rightval
  step 4: pop stack
    
    
