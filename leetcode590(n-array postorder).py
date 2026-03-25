


"""
# Definition for a Node."""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') :
        result = []
        
        # Helper function
        def traverse(node):
            # Base Case: If node is None, stop
            if not node:
                return
            
            # RECURSIVE STEP:
            # Instead of traverse(node.left), we loop through the list
            for child in node.children:
                traverse(child)
            
            # ROOT STEP:
            # After the loop finishes (all children visited), add the root
            result.append(node.val)
        
        traverse(root)
        return result









# Helper function to build tree from list representation (for local testing)
def build_tree_from_list(arr):
    """Build a binary tree from level-order list representation"""
    if not arr or arr[0] is None:
        return None
    
    root = Node(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            node.left = Node(arr[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(arr) and arr[i] is not None:
            node.right = Node(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,3,4,5,None,8,None,None,6,7,9]
    # Tree structure:
    #         1
    #       /   \
    #      2     3
    #     / \     \
    #    4   5     8
    #       / \   / \
    #      6   7 9   None
    arr = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
    root = build_tree_from_list(arr)
    
    result = solution.postorderTraversal(root)
    print(f"Input array: {arr}")
    print(f"Postorder traversal: {result}")
    print()
    
    # Visual representation
    print("Tree structure:")
    print("""
          1
        /   \\
       2     3
      / \\     \\
     4   5     8
        / \\   /
       6   7 9
    """)
    print(f"Postorder (Left → Right → Root): {result}")
    print(f"Expected: [4, 6, 7, 5, 2, 9, 8, 3, 1]")
        