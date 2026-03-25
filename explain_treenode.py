# ============================================
# EXPLAINING TreeNode(0) and TreeNode Representation
# ============================================

print("=" * 70)
print("TreeNode CLASS DEFINITION")
print("=" * 70)
print()

print("""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
""")
print()

print("=" * 70)
print("YOUR EXAMPLE TREE")
print("=" * 70)
print()

print("TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}")
print()
print("Visual representation:")
print("""
    1
     \\
      2
     /
    3
""")
print()

print("Structure:")
print("  - Root node: val=1")
print("  - left = None")
print("  - right = TreeNode(2)")
print("    - left = TreeNode(3)")
print("    - right = None")
print()

print("=" * 70)
print("WHAT IS TreeNode(0)?")
print("=" * 70)
print()

print("TreeNode(0) creates a SINGLE node:")
print("-" * 70)
print()
print("TreeNode(val=0, left=None, right=None)")
print()
print("Representation:")
print("  TreeNode{val: 0, left: None, right: None}")
print()

print("Visual representation:")
print("""
    0
""")
print()

print("This is just ONE node with:")
print("  - val = 0")
print("  - left = None (no left child)")
print("  - right = None (no right child)")
print()

print("=" * 70)
print("COMPARISON")
print("=" * 70)
print()

print("Your example tree:")
print("  TreeNode{val: 1, left: None, right: TreeNode{val: 2, ...}}")
print("  → A tree with 3 nodes (1, 2, 3)")
print()

print("TreeNode(0):")
print("  TreeNode{val: 0, left: None, right: None}")
print("  → A tree with just 1 node (0)")
print()

print("=" * 70)
print("DIFFERENT TreeNode CREATIONS")
print("=" * 70)
print()

# Let's create examples
print("Example 1: TreeNode(0)")
print("-" * 70)
print("  TreeNode(0)")
print("  → Creates: TreeNode{val: 0, left: None, right: None}")
print("  → A single node with value 0")
print()

print("Example 2: TreeNode(5)")
print("-" * 70)
print("  TreeNode(5)")
print("  → Creates: TreeNode{val: 5, left: None, right: None}")
print("  → A single node with value 5")
print()

print("Example 3: TreeNode with children")
print("-" * 70)
print("  node0 = TreeNode(0)")
print("  node1 = TreeNode(1)")
print("  node2 = TreeNode(2, left=node0, right=node1)")
print()
print("  → Creates a tree:")
print("""
      2
     / \\
    0   1
""")
print()

print("=" * 70)
print("REPRESENTATION FORMAT BREAKDOWN")
print("=" * 70)
print()

print("Format: TreeNode{val: X, left: Y, right: Z}")
print()
print("For TreeNode(0):")
print("  val: 0        → The value stored in the node")
print("  left: None    → No left child")
print("  right: None   → No right child")
print()

print("For a node with children:")
print("  val: 2")
print("  left: TreeNode{...}   → Points to another TreeNode")
print("  right: TreeNode{...}  → Points to another TreeNode")
print()

print("=" * 70)
print("CREATING TREES STEP BY STEP")
print("=" * 70)
print()

print("Method 1: Single node")
print("-" * 70)
print("  node = TreeNode(0)")
print("  → TreeNode{val: 0, left: None, right: None}")
print()

print("Method 2: Tree with children")
print("-" * 70)
print("  # Create leaf nodes")
print("  node0 = TreeNode(0)  # TreeNode{val: 0, left: None, right: None}")
print("  node1 = TreeNode(1)  # TreeNode{val: 1, left: None, right: None}")
print()
print("  # Create parent node")
print("  root = TreeNode(2, left=node0, right=node1)")
print("  → TreeNode{val: 2, left: TreeNode{...}, right: TreeNode{...}}")
print()

print("Visual:")
print("""
      2
     / \\
    0   1
""")
print()

print("=" * 70)
print("YOUR SPECIFIC QUESTION ANSWERED")
print("=" * 70)
print()

print("If your code has:")
print("  TreeNode{val: 1, left: None, right: TreeNode{val: 2, ...}}")
print()
print("Then TreeNode(0) would be:")
print("  TreeNode{val: 0, left: None, right: None}")
print()
print("It's just a single node with value 0 and no children.")
print()

print("=" * 70)
print("COMPLETE EXAMPLE")
print("=" * 70)
print()

# Actually create TreeNode class for demonstration
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

print("Creating TreeNode(0):")
node0 = TreeNode(0)
print(f"  {node0}")
print()

print("Creating your example tree:")
node3 = TreeNode(3)
node2 = TreeNode(2, left=node3)
node1 = TreeNode(1, right=node2)
print(f"  {node1}")
print()

print("Comparison:")
print(f"  TreeNode(0) = {node0}")
print(f"  Your tree root = {node1}")
print()



