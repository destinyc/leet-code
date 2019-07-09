
#所谓合并，即相应位置上的元素值想家
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def merge(root1, root2):
    if root1 and root2:
        root = TreeNode(root1.val + root2.val)
        root.left = merge(root1.left, root2.left)
        root.right = merge(root1.right, root2.right)

        return root
    else:

