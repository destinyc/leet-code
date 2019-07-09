
def _num(List):           #复杂度 n**2
    if len(List) < 3:
        return 0

    total = 0
    List.sort()

    for i in range(len(List) - 1, 1, -1):              #我们先固定住最大的边（固定最小的边试过了不行）
        left, right = 0, i - 1

        while left < right:
            if List[i] < List[left] + List[right]:          #看懂这个if else是关键
                total += right - left                    #这个区间的都可以
                right -= 1
            else:
                left += 1

    return total

if __name__ == '__main__':
    List = [1,2,3,4,5,6]            #答案是7
    print(_num(List))