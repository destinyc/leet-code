
#将1到n的平方的数螺旋的写入n乘n的矩阵

def Matrix(n):
    if n == 1:
        return [[1]]
    matrix = [[0] * n for _ in range(n)]
    index, num = 0, 1
    while index < n // 2 + 1:

        for i in range(index, n - index):
            matrix[index][i] = num
            num += 1
        for i in range(index + 1, n - index):
            matrix[i][n - index - 1] = num
            num += 1
        for i in range(n - index - 2, index - 1, -1):
            matrix[n - index - 1][i] = num
            num += 1
        for i in range(n - index - 2, index, -1):
            matrix[i][index] = num
            num += 1

        index += 1
    return matrix

if __name__ == '__main__':
    n = 4
    print(Matrix(n))