
#给一个m乘n的矩阵，每个数字表示路径值，求从左上到右下最小路径和(只能向下和向右)

#dp是个同样尺寸的矩阵，每个元素表示到当前格子时的最小路径

#关系： dp[column][row] = min(dp[column-1][row], dp[column][row-1]) + List[column][row]

#初始化
#       当column = 0时， dp[0][row] = dp[0][row-1] + List[0][row]
#       当row = 0时，    dp[column][0] = dp[column-1][0] + List[column][0]

def min_path(List):
    if List == []:
        return 0

    columns, rows = len(List), len(List[0])
    dp = [[0] * rows for _ in range(columns)]

    #初始化部分
    dp[0][0] = List[0][0]
    for column in range(1, columns):
        dp[column][0] = List[column][0] + dp[column - 1][0]
    for row in range(1, rows):
        dp[0][row] = List[0][row] + dp[0][row - 1]

    #动态规划部分
    for column in range(1, columns):
        for row in range(1, rows):
            dp[column][row] = min(dp[column-1][row], dp[column][row-1]) + List[column][row]

    return dp[-1][-1]


if __name__ == '__main__':
    List = [[1,3,1],[1,5,1],[4,2,1]]
    print(min_path(List))