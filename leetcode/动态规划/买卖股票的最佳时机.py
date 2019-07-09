
#第一版本 leetcode121  只能进行一次买入卖出

def _maxprofit(List):
    if len(List) == 0 or len(List) == 1:
        return 0
    min = List[0]         #时刻维持一个当前遍历过的最小值
    maxprof = 0
    for i in range(1, len(List)):
        prof = List[i] - min
        maxprof = max(maxprof, prof)

        if List[i] < min:
            min = List[i]

    return maxprof

# 按照第四个版本的动态规划思路

#dp是二维的（没有买入卖出次数那一维）
#dp[i][j]      #j只能取0，1, 2表示手里没有，今天买了一股，今天卖了一股,也就是我们直接把买卖次数那一维合并了过来

# 关系   dp[i][0] = dp[i-1][0]
#        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
#        dp[i][2] = dp[i-1][1] + prices[i]


#第二版本，可以无数次买卖，不是动态规划（当然也可以按照第四版一样动态规划）

def maxprofit2(prices):
    if len(prices) < 1:
        return 0
    output = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i-1] > 0:
            output += prices[i] - prices[i-1]

    return output


#第三版本，可进行两次交易
#稍微改一下dp的维度 dp[i][j][k]  j表示第几次买卖， k表示手中是否有股票

def maxprofit3(prices):
    if prices == []:
        return 0
    dp = [[[0] * 2 for _ in range(3)] for _ in range(len(prices))]       #dp[i][2][2]
    dp[0][0][0], dp[0][1][1], dp[0][2][1] = 0, - prices[0], 0

    for i in range(1, len(prices)):
        for j in range(1, 3):
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])


    print(dp)
    return max([dp[len(prices) - 1][j][0] for j in range(3)])











#第四版本，可以进行k次买卖，最难的一道，动态规划矩阵需要三维才可以存储所有信息

#于是，这道题的解法还可以可用于上面的三道

# dp[i][j][l]     #i是第几天，j是这天手中是否有股票（0表示没，1表示有），l是已经买卖的股票次数，dp是最大利润


#关系（最复杂的部分）

# for i in range(len(prices)):        for l in range (k+1):
# dp[i] [0] [l] = max(dp[i-1][0][l], dp[i-1][1][l-1] + prices[i])     #要想明白这两个状态转移方程
# dp[i] [1] [l] = max(dp[i-1][0][l-1] - prices[i], dp[i-1][1][l])

#在上面的dp中，这道题是每次买之前必须把手里的卖出去


#动态规划
def maxprofit4(prices, k):
    pass



#这里额外加一个第四版本的升级版：手里可以同时有X个股票

#于是dp的j这个维度就不仅仅是0和1了
# for i in range(len(prices)):        for l in range (k+1):     for j in range(X):

# dp[i][j][l] = max(dp[i-1][j][l], dp[i-1][j+1][l-1] + prices[i], dp[i-1][j-1][l-1] - prices[i])

#这里只是简单的说一下，就不写了
def maxproif_(proces, k, X):
    pass




if __name__ == '__main__':
    # List = [3,3,5,0,0,3,1,4]
    # print(maxprofit3(List))

    #leetcode923
    def threeSumMulti(A, target):
        A.sort()
        total_num = 0
        for i in range(len(A) - 2):

            left, right = i + 1, len(A) - 1
            while left < right:
                print(i, left, right)
                add = A[i] + A[left] + A[right]

                if add == target:
                    if A[left] == A[right]:
                        total_num += (right - left) * (right - left + 1) // 2
                        break
                    else:
                        current_left = left
                        while current_left + 1 < right and A[current_left] == A[current_left + 1]:
                            current_left += 1

                        current_right = right
                        while current_left < current_right - 1 and A[current_right] == A[current_right - 1]:
                            current_right -= 1

                        left_num, right_num = current_left - left + 1, right - current_right + 1
                        total_num += left_num * right_num

                        left, right = current_left + 1, current_right - 1
                    # else:
                    #     left_num, right_num = 1, 1
                    #     left += 1
                    #     while left < right and A[left] == A[left - 1]:
                    #         left_num += 1
                    #         left += 1
                    #
                    #     right -= 1
                    #     while left < right and A[right] == A[right + 1]:
                    #         right_num += 1
                    #         right -= 1
                    #     print(A[i], A[left], A[right], 'accure:', left_num * right_num)
                    #     total_num += left_num * right_num

                elif add < target:
                    left += 1
                else:
                    right -= 1

        return total_num % (10 ** 9 + 7)

    # A = [1,1,2,2,3,3,4,4,5,5]
    # target = 8
    A = [0,2,0]
    target = 2
    print(threeSumMulti(A, target))
