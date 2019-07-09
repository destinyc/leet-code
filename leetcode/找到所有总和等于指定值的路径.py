
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_all(node, current_sum, path, output):
    is_leaf = node.left is None and node.right is None
    if is_leaf and current_sum == node.val:
        output.append(path)

    if node.left:
        find_all(node.left, current_sum - node.val, path + [node.left.val], output)
    if node.right:
        find_all(node.right, current_sum - node.val, path + [node.right.val], output)


def find(tree, sum):
    if tree is None:
        return []

    path = [tree.val]
    output = []

    find_all(tree, sum, path, output)

    return output

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(2)

    print(find(root, 4))