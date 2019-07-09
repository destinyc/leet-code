
#将一个字符串转换成另一个字符串使用的最少操作数，每次操作可以插入、删除、替换

#应该用二维dp矩阵
#dp[i][j]表示从word1的前i个元素到word2的前j个元素的编辑距离

#关系 dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1,  dp[i-1][j-1] + (0或者1在word1[i] == word2[j]的情况下))

#初始化 dp[0][j] = j   dp[i][0] = i

def min_change(word1, word2):
    dp = [[0] * (len(word2)+1) for _ in range(len(word1) + 1)]

    for i in range(len(word1) + 1):
        dp[i][0] = i

    for j in range(len(word2) + 1):
        dp[0][j] = j

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1,  dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))

    return dp[-1][-1]

if __name__ == '__main__':
    word1 = 'horse'
    word2 = 'ros'
    print(min_change(word1, word2))


















