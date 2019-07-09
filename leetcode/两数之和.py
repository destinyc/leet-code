
#输入一个数组和一个数，找到数组中的一对儿使得他们的和等于给定数,返回两数索引

def find(List, k):                    #方法1

    dic = {}
    for index, num in enumerate(List):
        diff = k - num
        if diff in dic:
            return [dic[diff], index]

        dic[num] = index

    return None


#双指针法

def _find(List, k):                     #前提是排序的数组
    begin, end = 0, len(List) - 1

    while begin < end:
        add = List[begin] + List[end]
        if add == k:
            return [begin, end]
        elif add > k:                   #这两个数偏大了，酒吧尾部的指针往前移
            end -= 1
        else:
            begin += 1

    return None

