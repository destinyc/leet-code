
#所谓旋转排序数组，就是排序的数组中的前几个元素移到了后边,如[1,2,3,4,5,6]变成[4,5,6,1,2,3]
#返回查找元素对应的索引，或者-1

def search_center(List):    #先找到旋转中心的坐标（相当于上一题查找旋转数组的最小值）
    if List == []:
        return None
    if List[0] <= List[-1]:      #根本没有旋转或者只有一个元素
        return 0

    begin, end = 0, len(List) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if List[mid] < List[mid - 1]:
            return mid

        if List[mid - 1] < List[mid] and List[mid] > List[-1]:
            begin = mid + 1

        else:
            end = mid - 1

def search(List, target):
    if List == []:
        return None

    center = search_center(List)
    if target > List[-1]:
        begin, end = 0, center - 1
    else:
        begin, end = center, len(List) - 1

    while begin <= end:
        mid = (begin + end) // 2
        if List[mid] == target:
            return mid
        elif List[mid] > target:
            end = mid - 1
        else:
            begin = mid + 1

    return -1

if __name__ == '__main__':
    List = [3,1]
    target = 1
    print(search(List, target))
