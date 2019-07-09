
#leetcode141 判断链表是否有环

def judgement(ListNode):

    current, prev = ListNode, ListNode          #一个一次跑一步，另一个跑两步
    while prev:
        if prev.next is None:
            return False
        current = current.next
        prev = prev.next.next

        if current == prev:
            return True

    return False



#leetcode142 找到环形链表的入口
#粗暴法，也可以用来判断是否有环
def find(ListNode):
    if ListNode is None:
        return None
    List = []
    while ListNode:
        if ListNode in List:
            return ListNode
        List.append(ListNode)
        ListNode = ListNode.next

    return None


#创新法
#上面我们提到的两个快慢指针他们相遇时一定在环内,我们对他进行小的改动
def _judgement(ListNode):
    if ListNode is None:
        return None
    current, prev = ListNode, ListNode
    while prev:
        if prev.next is None:
            return None
        prev = prev.next.next
        current = current.next

        if prev == current:
            return prev             #我们将这个环中的节点返回

    return None

def _find(ListNode):
    node = _judgement(ListNode)
    if node is None:
        return None

    listnode = node.next
    length = 1
    while listnode != node:           #我们从这里得到环的节点数
        length += 1
        listnode = listnode.next

    current, prev = ListNode, ListNode
    for i in range(length):                #让一个指针先走环的节点的个数步
        prev = prev.next

    while prev != current:
        current, prev = current.next, prev.next

    return prev


























