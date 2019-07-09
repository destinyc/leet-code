def FindPath(root, num):
    current_sum = 0
    path, output = [], []
    Find(output, root, num, path, current_sum)

    return output


def Find(output, root, num, path, current_sum):
    current_sum += root.value
    path.append(root.value)          #将当前节点的值加上并入栈

    #判断是否已经到达了叶节点
    is_Leaf = (root.left is None and root.right is None)

    if (current_sum == num and is_Leaf):              #到达了叶节点，并且当前路径的总值等于给定数值
        output.append(path)

    #不是叶节点就继续往下走
    if root.left:
        Find(output, root.left, num, path, current_sum)
    if root.right:
        Find(output, root.right, num, path, current_sum)

    #当前路径已经到底了，弹出叶节点来返回上一个节点，并从总和中减去节点值
    node_value = path.pop()
    current_sum -= node_value