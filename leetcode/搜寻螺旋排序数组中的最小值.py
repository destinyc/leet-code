
#所谓螺旋排序数组：[1,2,3,4,5,6,7] 变成 [4,5,6,7,1,2,3]
#注意这里数组中不包含重复元素，返回索引

def search(List):
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



if __name__ == '__main__':
    List = [3,1]
    print(search(List))