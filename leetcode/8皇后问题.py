

def queue(n):
    ColumnIndex = [i for i in range(n)]     #这个列表，index表示的是棋盘的行，数值对应的就是这行上皇后的列
    output = []                             #然后找这个列表的全排列就是所有的 皇后不同行同列 的情况
    path = []
    quanpailie(ColumnIndex, output, path)

    jieguo = []
    for item in output:
        if duijiaoxian(item, n):
            jieguo.append(item)

    jieguo_ = []
    for item in jieguo:
        board = []
        for num in item:
            s = ['.'] * 8
            s[num] = 'Q'
            board.append(''.join(s))

        jieguo_.append(board)

    print(jieguo_)




def duijiaoxian(List, n):
    for i in range(n - 1):
        for j in range(i + 1, n):
            if j - i == abs(List[i] - List[j]):
                return False

    return True

def quanpailie(List, output, path):                #核心还是全排列
    if len(List) == 0:
        output.append(path)

    else:
        for i in range(len(List)):
            quanpailie(List[:i] + List[i+1:], output, path + [List[i]])




if __name__ == '__main__':
    num = 4                   #皇后个数
    queue(num)