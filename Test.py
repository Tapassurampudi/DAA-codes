class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    if root is None:
        return []

    result = []  
    queue = [root]  

    while queue:
        current_level = []  

        for _ in range(len(queue)):
            node = queue.pop(0) 
            current_level.append(node.val)

            if node.left:
                queue.append(node.left) 
            if node.right:
                queue.append(node.right) 

        result.append(current_level)  

    return result
