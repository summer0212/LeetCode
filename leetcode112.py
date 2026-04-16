# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        remaining_budget = targetSum - root.val

        left_result = self.hasPathSum(root.left, remaining_budget)
        right_result = self.hasPathSum(root.right, remaining_budget)

        return left_result or right_result


        