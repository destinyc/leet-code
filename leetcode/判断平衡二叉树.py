def depth(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1

    return max(depth(root.left), depth(root.right)) + 1

#递归法:平衡二叉树即左右子树深度绝对值小于1
def is_Balanced(root):
    if root is None:
        return True

    if abs(depth(root.left) - depth(root.right)) <= 1:
        return is_Balanced(root.left) and is_Balanced(root.right)       #递归判断子树

    return False