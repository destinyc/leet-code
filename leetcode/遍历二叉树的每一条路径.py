class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#使用递归
def find(root, path, output):
    if root.left is None and root.right is None:
        output.append(path)

    if root.left:
        find(root.left, path + [root.left.val], output)
    if root.right:
        find(root.right, path + [root.right.val], output)

def path(tree):
    if tree is None:
        return []
    if tree.left is None and tree.right is None:
        return [tree.val]

    path = [tree.val]
    output = []

    find(tree, path, output)
    return output


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(path(root))

