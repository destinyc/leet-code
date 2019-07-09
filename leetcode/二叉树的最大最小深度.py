
#深度指的是叶节点的深度

#最大深度
def max_depth(root):
    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))            #递归一句话

#最小深度
def min_depth(root):

    if root is None:
        return 0
    if root.left is None:
        return 1 + min_depth(root.right)                #同样用递归，但是要分四种不同的情况考虑
    if root.right is None:
        return 1 + min_depth(root.left)

    return 1 + min(min_depth(root.left), min_depth(root.right))