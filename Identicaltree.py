class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def are_identical_trees(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return (root1.value == root2.value and
            are_identical_trees(root1.left, root2.left) and
            are_identical_trees(root1.right, root2.right))


tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(6)
tree2.left.left = TreeNode(4)

if are_identical_trees(tree1, tree2):
    print("The two trees are identical.")
else:
    print("The two trees are not identical.")