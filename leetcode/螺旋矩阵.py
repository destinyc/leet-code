
def _bianli(List, rows, columns, index):   #这个函数根据index位置遍历这一圈

    #正向先走第一行
    output = []
    for i in range(index, columns - index):
        output.append(List[index][i])

    #当前要遍历的一圈大于等于两行时才有向下的遍历
    if rows - index - 1 > index:
        for i in range(index + 1, rows - index):
            output.append(List[i][columns - index - 1])

    #同样当这一圈大于等于两列时才存在回去的行
    if columns - index - 1 > index:
        for i in range(columns - index - 2, index - 1, -1):
            output.append(List[columns - index - 1][i])

    #当这一圈大于等于 三行 时才存在向上的遍历
    if rows - index - 2 > index:
        for i in range(rows - index - 2, index, -1):
            output.append(List[i][index])

    return output

def bianli(List):
    if List == []:
        return []

    rows, columns = len(List), len(List[0])
    output = []
    index = 0                  #这个索引对应第几个左上角，我们从这个左上角开始走一圈
    while index * 2 < rows and index * 2 < columns:              #开始一圈一圈的遍历
        output.extend(_bianli(List, rows, columns, index))
        index += 1

    return output


if __name__ == '__main__':
    List = [[1,2,3], [4,5,6],[7,8,9]]
    print(bianli(List))