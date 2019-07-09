
#简单思路：递归
def digui(root1, root2):
    if root1 and root2:
        #这一句是核心，对称二叉树的左子树的左子树等于右子树的右子树
        return root1.val == root2.val and digui(root1.left, root2.right) and digui(root1.right, root2.left)
    else:
        return not root1 and not root2

def caculate(tree):
    if tree is None:
        return True
    else:
        return digui(tree.left, tree.right)




