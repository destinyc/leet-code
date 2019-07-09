
#这道题还可以先将两个链表全取出来，然后倒叙遍历，直到遇到不相等的点，则后面的点就是要找的第一个公共节点

def getIntersectionNode(headA, headB):
    """
    注意，两个链表相交，那么从某个节点开始，直到结尾就是这两个链表的公共链表
    :type head1, head1: ListNode
    :rtype: ListNode
    """

    lengthA, lengthB = 0, 0
    node = headA
    while node is not None:
        lengthA += 1
        node = node.next

    node = headB
    while node is not None:
        lengthB += 1
        node = node.next

    if lengthA >= lengthB:
        diff = lengthA - lengthB

        nodeA, nodeB = headA, headB
        for i in range(diff):        #先让相对较长的链表先走到剩余短链表长度的位置，然后开始两个一起走，找到第一个相等的节点
            nodeA = nodeA.next

        while nodeA is not None and nodeB is not None:
            if nodeA == nodeB:
                return nodeA

            nodeA, nodeB = nodeA.next, nodeB.next
    else:
        diff = lengthB - lengthA

        nodeA, nodeB = headA, headB
        for i in range(diff):
            nodeB = nodeB.next

        while nodeA is not None and nodeB is not None:
            if nodeA == nodeB:
                return nodeA

            nodeA, nodeB = nodeA.next, nodeB.next

    return None