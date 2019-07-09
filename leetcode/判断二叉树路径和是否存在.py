#给定一个二叉树和一个值，判断是否存在一条路径使得和等于这个值

#使用递归
def judgement(tree, num):
    if tree is None:
        return False

    is_leaf = (tree.left is None and tree.right is None)

    if is_leaf and tree.val == num:
        return True
    if is_leaf and tree.val != num:
        return False

    return judgement(tree.left, num - tree.val) or judgement(tree.right, num - tree.val)
