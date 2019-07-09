
def bianli(tree):
    output = []
    if tree is None:
        return output

    stack = [[tree, 0]]

    while stack:
        [node, line_index] = stack.pop(0)
        if node is None:
            continue

        if line_index > len(output):
            output.append([node.val])
        else:
            output[line_index].append(node.val)

        stack.append([node.left, line_index + 1])
        stack.append([node.right, line_index + 1])

    return output


#前序遍历，一直向左走，并将右节点入栈
def _bianli(root):
    if root is None:
        return []

    stack, output = [], []
    while stack != [] or root:
        while root:
            stack.append(root.right)           #右子树入栈，一直往左走
            output.append(root.val)
            root = root.left

        root = stack.pop()
    return output

#中序遍历, 先一直往左下走到底并把路径入栈
def bl(root):
    if root is None:
        return None
    stack, output = [], []
    while stack != [] or root:
        if root:
            stack.append(root)         #一直左下走到底并把路径入栈
            root = root.left

        else:
            root = stack.pop()
            output.append(root.val)        #把节点的值保存后进入右子树
            root = root.right

    return output
















