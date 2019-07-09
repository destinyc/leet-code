
#输入零钱面值的List和总金额
#返回需要的最少的面值是多少

#距离 List = [1,2,5], amount = 11  结果是3  ：1+5+5

#我们吧这个题变形一下，爬楼梯，每次可以爬的阶数是coins中的元素，爬到顶最少步数

#dp[i]是上到第i台阶的最小步数
#关系 ： dp[n] = min(dp[n - item] for item in coins) + 1
#初始化dp[0] = 0,其他的都是amount + 1（即最大情况面值全是1）

#注意dp有amount+1个元素，因为第一个元素是0元

def min_(coins, amount):
    if coins == [] and amount == 0:
        return 0
    if coins == [] or amount == 0:
        return -1

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for num in coins:
            if num <= i:
                dp[i] = min(dp[i - num] + 1, dp[i])
    if dp[amount] > amount:
        return -1

    return dp[amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(min_(coins, amount))

