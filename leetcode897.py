class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Create a dummy head node.
        # This simplifies handling the very first node of the new tree.
        dummy_head = TreeNode(0)

        # Step 2: 'current_new_node' will always point to the last node
        # that was added to our flattened tree. Start it at the dummy.
        self.current_new_node = dummy_head

        # Step 3: Perform an in-order traversal
        self._inorder_flatten(root)

        # After traversal, dummy_head.right will be the root of our new flattened tree.
        return dummy_head.right

    # This is our recursive helper function for in-order traversal and flattening
    def _inorder_flatten(self, node):
        if node is None:
            return

        # 1. Go LEFT: Recursively flatten the left subtree
        # This will process the leftmost nodes first
        self._inorder_flatten(node.left)

        # 2. Visit Current Node (ROOT): This is where the rearrangement happens.
        #    a. Set the current node's left child to None (as per problem rules).
        node.left = None

        #    b. Link the *previous* flattened node's right child to the *current* node.
        self.current_new_node.right = node

        #    c. Move our 'current_new_node' pointer to the node we just processed.
        #       This ensures it's ready to link to the *next* node in in-order sequence.
        self.current_new_node = node

        # 3. Go RIGHT: Recursively flatten the right subtree
        self._inorder_flatten(node.right)