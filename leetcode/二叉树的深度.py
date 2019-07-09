
def max_depth(tree):
    if tree is None:
        return 0
    if tree.left is None and tree.right is None:
        return 1

    return 1 + max(max_depth(tree.left), max_depth(tree.right))



#同理N叉树的深度
def _max_depth(tree):
    if tree is None:
        return 0
    if tree.children is None:
        return 1

    return 1 + max(max_depth(node) for node in tree.children)