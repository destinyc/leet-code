
#dp[i]保存的是到这一个阶梯话费的最小体力

#那么 dp[n] = min(dp[n-1], dp[n-2]) + List[n]
#最终返回的是后两项中小的那个

def cost(List):
    if List == []:
        return 0
    if len(List) == 1:
        return List[-1]
    dp = [0] * len(List)
    dp[0], dp[1] = List[0], List[1]

    for i in range(2, len(List)):
        dp[i] = min(dp[i-1], dp[i-2]) + List[i]

    return min(dp[-1], dp[-2])


if __name__ == '__main__':
    List = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(cost(List))