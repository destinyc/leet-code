
#看到二叉树就先思考一下递归
def _sum(root):
    if root is None:
        return 0

    if root.left and root.left.left is None and root.left.right is None:
        return root.left.val + _sum(root.right)           #是左叶节点，就把它的值加上右子树的左叶节点

    else:
        return _sum(root.left) + _sum(root.right)

