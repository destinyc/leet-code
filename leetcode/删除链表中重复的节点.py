
#在一个排序链表中删除重复的节点（122334变成14）
#leetcode82
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#暴力法
def delete(head):
    dic, List = {}, []
    if head is None:
        return None
    while head:
        if head.val in dic:
            dic[head.val] += 1
        else:
            dic[head.val] = 1
        List.append(head.val)
        head = head.next

    head = ListNode(None)
    node = head
    for num in List:
        if dic[num] == 1:
            node.next = ListNode(num)
            node = node.next

    return head.next


#直接改变链表指针
def _delete(head):
    guard = ListNode(None)
    guard.next = head

    current, prev = guard, guard
    while prev:
        if prev.next and prev.next.val == prev.val:
            while prev.next and prev.next.val == prev.val:
                prev = prev.next

            current.next = prev.next
            prev = prev.next

        else:
            current = prev
            prev = prev.next

    return guard.next




















