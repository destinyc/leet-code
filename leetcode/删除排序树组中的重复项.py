
#在数组原地修改，将不重复的元素放最前面，忽略多余的部分，返回不重复元素的个数

def find(List):
    if List == []:
        return 0

    current_num = List[0]
    index = 1
    for num in List[1:]:
        if num == current_num:
            continue
        else:
            current_num = num
            List[index] = num
            index += 1

    return index

if __name__ == '__main__':
    List = [1,2,3,4,4,4,5,6]
    length = find(List)
    print(length)
    print(List)