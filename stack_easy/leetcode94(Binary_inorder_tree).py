# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root) :
        result = []

        def traverse(node): # This is the recursive helper function
            if node is None: # Base Case
                return

            # 1. Go LEFT
            traverse(node.left)

            # 2. Visit Current Node (ROOT)
            result.append(node.val)

            # 3. Go RIGHT
            traverse(node.right)

        traverse(root) # Initial call starts the recursion
        return result
        

#NOTE :-
# In essence, the setup code (node3 = TreeNode(3) etc.) was for us to create a tree to test our function locally. On LeetCode, that setup is done for you.
# So, when you see root: Optional[TreeNode], just imagine that root variable is already pointing to the TreeNode object that represents the 10 in our example tree, and all its children (5, 15, 3, 7, etc.) are already correctly linked via left and right pointers. You just need to write the logic to traverse it.

'''TreeNode Representation
Checking node TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}
Just checking None
Checking node None
Checking node TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}
Just checking TreeNode{val: 3, left: None, right: None}
Checking node TreeNode{val: 3, left: None, right: None}
Just checking None
Checking node None
Checking node None
Checking node None'''