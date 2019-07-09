

def find(tree, node, path):            #全局变量path的初始值是[tree]
    if tree == node:
        return True
    if tree.left:
        path.append(tree.left)
        if find(tree.left, node, path):       #说明节点在tree的左子树上
            return True
        else:                                 #否则就把左子树节点弹出
            path.pop()
    if tree.right:
        path.append(tree.right)
        if find(tree.right, node, path):
            return True
        else:
            path.pop()

    return False
