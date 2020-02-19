#######################################################################################
# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under
#  it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees (roots 1,1,1,1,0)
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
########################################################################################

class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __repr__(self):
        return str(self.data)

def count_unival_trees(root):
    if not root:
        #if root is null
        return 0
    elif not root.left  and not root.right:
        #right and left are empty it is unival tree
        return 1
    elif not root.left and root.right.data==root.data:
        #if left is null and root and right has same data cnt it 1 and check  right side
        return 1 + count_unival_trees(root.right)
    
    elif not root.right and root.left.data==root.data:
        #if right is null and root and left has same data cnt it 1 and check  left side
        return 1 + count_unival_trees(root.left)

    else:
        
        #check current node
        current_node_count = 0
        if root.data == root.left.data and root.data == root.left.data:
            current_node_count = 1
        
        #calculate child cnt
        child_counts=count_unival_trees(root.left) + count_unival_trees(root.right)

        #Add both and return
        return current_node_count + child_counts
        


if __name__ == "__main__":
    node_a = Node('0')
    node_b = Node('1')
    node_c = Node('0')
    node_d = Node('1')
    node_e = Node('0')
    node_f = Node('1')
    node_g = Node('1')
    node_a.left = node_b
    node_a.right = node_c
    node_c.left = node_d
    node_c.right = node_e
    node_d.left = node_f
    node_d.right = node_g

    assert count_unival_trees(None) == 0
    assert count_unival_trees(node_a) == 5
    assert count_unival_trees(node_c) == 4
    assert count_unival_trees(node_g) == 1
    assert count_unival_trees(node_d) == 3

    print(count_unival_trees(node_a))
