# 给定二叉树中的两个节点，找到最近的公共祖先（返回的是Node类型）

def find_path(root, path, node):
    if root == node:
        return True
    if root.left:
        path.append(root.left)
        if find_path(root.left, path, node):
            return True
        else:
            path.pop()
    if root.right:
        path.append(root.right)
        if find_path(root.right, path, node):
            return True
        else:
            path.pop()

    return False


def lowestCommonAncestor(root, p, q):
    if root is None:
        return None
    if p == q:
        return p

    path1, path2 = [root], [root]
    find1, find2 = find_path(root, path1, p), find_path(root, path2, q)
    if find1 == False or find2 == False:
        return None
    index = 0

    # 注意，只要两个节点出现在同一个树中，那么一定存在这个最近父节点。
    while index < len(path1) and index < len(path2) and path1[index] == path2[index]:
        index += 1

    return path1[index - 1]
