
def findFristIndex(List, num):            #这个函数用二分查找来找这个数的起始索引
    if len(List) == 0:
        return 0
    begin, end = 0, len(List) - 1

    while begin <= end:
        mid = (end + begin) // 2

        if List[mid] < num:
            begin = mid + 1
        elif List[mid] > num:
            end = mid - 1

        else:
            if mid == 0 or List[mid] != List[mid - 1]:         #这个判定条件是关键
                return mid
            else:
                end = mid - 1
    return -1     #没有找到这个数

def findLastIndex(List, num):             #同样，这个函数找结尾索引
    if len(List) == 0:
        return 0
    begin, end = 0, len(List) - 1

    while begin <= end:
        mid = (end + begin) // 2

        if List[mid] < num:
            begin = mid + 1
        elif List[mid] > num:
            end = mid - 1
        else:
            if mid == len(List) - 1 or List[mid] != List[mid + 1]:        #注意判定条件
                return mid
            else:
                begin = mid + 1
    return -1    #并没有找到这个数


def count(List, num):
    if len(List) == 0:
        return 0

    begin_index = findFristIndex(List, num)
    end_index = findLastIndex(List, num)

    if begin_index != -1 and end_index != -1:
        return end_index - begin_index + 1

    return 0     #没有找到这个数

if __name__ == '__main__':
    List = [3,6,6,6,6,6,6,6,7,8,9]
    num = 10
    print(count(List, num))
