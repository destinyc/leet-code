
def quit_sort(List):

    qsort_rec(List, 0, len(List) - 1)

def qsort_rec(List, start, end):
    if start >= end:
        return
    i, j = start, end

    num = List[i]
    while j > i:
        while j > i and List[j] >= num:            #我们要找到第一个比num小的数放到i的位置
            j -= 1
        if i < j:
            List[i] = List[j]

        while j > i and List[i] <= num:             #我们要找到第一个比num小的数放到刚刚的j的位置
            i += 1
        if i < j:
            List[j] = List[i]


    List[i] = num                                  #i位置（等同于j位置）的值已经确定下来了不用再变了
    qsort_rec(List, start, i - 1)
    qsort_rec(List, i + 1, end)

if __name__ == '__main__':
    List = [4,5,3,2,1,7,9,6,8]

    quit_sort(List)
    # print(List)





