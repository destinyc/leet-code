#这个题分三种情况，二叉搜索树、含有指向父节点的树，不含指向父节点的树

#显示第一种情况：二叉搜索树

def find_node(tree, node1, node2):
    '''
    根据搜索树的特点，可以从根节点遍历，确定当前节点的值和两个节点的值的大小关系
    当找到第一个节点使得这个节点的值在两个节点的值中间时就是要找的节点
    '''
    if tree is None:
        return None

    if node1 == node2:
        return node1
    val1, val2 = node1.val, node2.val
    if val1 > val2:
        max_val, min_val = val1, val2
    else:
        max_val, min_val = val2, val1

    while tree:
        current_val = tree.val

        if current_val > max_val :               #两个节点都在左子树上
            tree = tree.left
        elif current_val < min_val:
            tree = tree.right
        else:
            return tree

    return None


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


#第二种情况：含有指向父节点指针的树

def compare_List(List1, List2):                  #找两个列表的第一个公共节点
    if List1 == [] or List2 == []:
        return None

    if len(List1) >= len(List2):
        diff = len(List1) - len(List2)

        for i in range(len(List2)):
            if List1[diff + i] == List2[i]:
                return List2[i]

        return None

    else:
        diff = len(List2) - len(List1)

        for i in range(len(List1)):
            if List2[diff + i] == List1[i]:
                return List1[i]

        return None



def _find_node(tree, node1, node2):
    '''
    将两个节点向上遍历直到根节点，形成了两个列表
    问题就变成了找两个列表的第一个相同节点
    '''

    if tree is None:
        return None
    if node1 == node2:
        return node1

    #生成第一个列表，列表中保存的是tree_node
    List1 = []
    while node1:
        List1.append(node1)
        node1 = node1.father

    #生成第二个链表
    List2 = []
    while node2:
        List2.append(node2)
        node2 = node2.father

    return compare_List(List1, List2)



#第三种情况：没有指向父节点的指针，也是通用的情况
def find_path(tree, node, path):
    '''

    :param tree: 当前遍历到了哪个节点
    :param node:
    :param path: 最后一个元素就是tree
    :return:
    '''
    if tree == node:
        return True
    if tree.left:
        path.append(tree.left)      #探索左子树
        if find_path(tree.left, node, path):         #在左子树上找到了
            return True
        else:
            path.pop()              #没找到，说明这个节点不在路径

    if tree.right:                  #重新探索右子树
        path.append(tree.right)
        if find_path(tree.right, node, path):
            return True
        else:
            path.pop()

    return False


def _find_node_(tree, node1, node2):
    '''
    从父节点逐个遍历，生成到两个节点的两个列表，这一步是这个方法的难点
    然后又变成了找两个列表的第一个公共元素
    '''
    if tree is None:
        return None
    if node1 == node2:
        return node1

    path1, path2 = [tree], [tree]
    find1 = find_path(tree, node1, path1)
    find2 = find_path(tree, node2, path2)

    if find1 == False or find2 == False:
        return None
    else:
        index = 0
        while path1[index] == path2[index]:
            output = path1[index]
            index += 1

    return output

























