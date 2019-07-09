
#输入是一个三角形状的二元列表（第一个一个元素，第二个两个元素。。。）
#从顶点往下走，每次只能走到下一行与它相邻的节点(即左下和右下两个)

#本来按照思路，我们的dp也应该是二维的，维护每一行的每一个点，但是题目要求最小化空间复杂度，于是：

#dp[0] = triangle[0][0]
#我们对每一行都维持一个dp，长度是每行元素数目
# 每次当前行循环结束后抛弃上一行的dp使用当前行的dp来计算下一行，就可以最小化空间复杂度

#关系：
#dp_[i] = min(dp[i], dp[i-1]) + List[column][i]             #dp_是当前正在计算的行，dp是上一行
#dp_[0] = dp[0] + List[column][0]       dp_[-1] = dp[-1] + List[column][-1]

#我看别人都是从下往上规划的，即先初始化最后一行的dp，这样关系更清晰一点，代码更简单一点

def min_path(triangle):
    if len(triangle) == 0:
        return 0

    dp = [triangle[0][0]]           #dp维护的是上一行的结果


    for column in range(1, len(triangle)):       #计算当前行的结果
        dp_ = [0] * (column + 1)
        dp_[0], dp_[-1] = dp[0] + triangle[column][0], dp[-1] + triangle[column][-1]
        for j in range(1, column):
            dp_[j] = min(dp[j], dp[j - 1]) + triangle[column][j]

        dp = dp_[:]
    return min(dp)

if __name__ == '__main__':
    triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    print(min_path(triangle))
