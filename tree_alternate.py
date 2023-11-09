class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_alternate_levels(root):
    if not root:
        return

    queue = [root]
    level = 0

    while queue:
        level_size = len(queue)
        print(f"Level {level}: ", end="")

        for i in range(level_size):
            node = queue.pop(0)
            print(node.value, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print()
        level += 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)

print("Alternate Levels of the Tree:")
print_alternate_levels(root)