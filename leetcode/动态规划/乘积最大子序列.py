
#找出乘积最大的连续子序列,返回积

#dp = [0] * len(nums)  一维的dp，每个元素表示将当前index的nums用上的情况下的最大的乘积

#关系  dp[i] = max(nums[i], dp[i - 1] * nums[i])
#初始化 dp[0] = nums[0]

# 额，结果不对，事情似乎没那么简单（如果当前值为负数那就一定用不上？答案是否定的）
# 所以 dp[length][2]  应该是二维的，第一位是用上当前值的话的最大乘积，另一个是最小乘积

#关系 当当前数值大于0时：   dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i])   dp[i][1] = min(dp[i - 1][1] * nums[i], nums[i])
        #小于0时:           dp[i][0] = max(dp[i - 1][1] * nums[i], nums[i])   dp[i][1] = min(dp[i - 1][0] * nums[i], nums[i])

# 初始值  dp[0][0], dp[0][1] = nums[0], nums[0]

def max_mul(nums):
    if nums == []:
        return 0

    # dp = [0] * len(nums)
    # dp[0] = nums[0]
    # for i in range(1, len(nums)):
    #     dp[i] = max(nums[i], dp[i - 1] * nums[i])
    #
    # return max(dp)

    dp = [[0] * 2 for _ in range(len(nums))]
    dp[0][0], dp[0][1] = nums[0], nums[0]

    for i in range(1, len(nums)):
        if nums[i] > 0:
            dp[i][0] = max(dp[i - 1][0] * nums[i], nums[i])
            dp[i][1] = min(dp[i - 1][1] * nums[i], nums[i])
        else:
            dp[i][0] = max(dp[i - 1][1] * nums[i], nums[i])
            dp[i][1] = min(dp[i - 1][0] * nums[i], nums[i])

    return max([item[0] for item in dp])





if __name__ == '__main__':
    nums = [-2,0,-1]
    print(max_mul(nums))