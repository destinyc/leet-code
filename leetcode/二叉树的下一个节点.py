
#描述，给定一个节点，给出中序遍历时的下一个节点

def find(root, node):
    if root is None:
        return None

    if node.right:          #如果这个节点存在右子树，那么下个节点就是右子树的最左边节点
        root = node.right
        while root:
            root = root.left

        return root

    else:
        while node.parent.right == node:        #不存在右子树，就一直向上直到当前结点不属于父节点的右节点为止，输出这个父节点
            node = node.parent

        return node.parent

