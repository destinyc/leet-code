class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def Convert(root, pLastNodeInList):
    '''

    :param root: 递归的子树根节点
    :param pLastNodeInList:永远指向双向链表的尾部节点
    :return:
    '''
    if root == None:
        return None

    pCurrent = root

    if pCurrent.left != None:               #先递归的把左侧子树全部转换成链表，而pLastNodeInList结束后就是链表尾部
        Convert(pCurrent.left, pLastNodeInList)

    pCurrent.left = pLastNodeInList         #把父节点添加到左子树链表的尾部
    if pLastNodeInList != None:
        pLastNodeInList.right = pCurrent

    pLastNodeInList = pCurrent             #此时链表尾部就变成了父节点
    if pCurrent.right != None:
        Convert(pCurrent.right, pLastNodeInList)       #把左子树的尾部节点和右子树最小的点连起来

#这里放上中序遍历做对比
def bianli(root):
    output = []
    if root is None:
        return output
    output.extend(bianli(root.left))
    output.extend([root.val])
    output.extend(bianli(root.right))

    return output

def Convert_tree(root):
    pLastNodeInList = TreeNode(None)
    Convert(root, pLastNodeInList)
    node = pLastNodeInList

    #找到生成的链表的头部节点并返回
    while node != None and node.left != None:
        node = node.left

    return node



