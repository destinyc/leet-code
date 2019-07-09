
#先是暴力查找,复杂度 三次方

def _total(List):
    if List == []:
        return 0
    total = 0
    for i in range(len(List)):
        for j in range(i + 1, len(List) + 1):
            if List[i : j] == List[i : j][::-1]:    #这一句的复杂度不是1
                total += 1

    return total



#这次的动态规划，dp就不再是一维的列表了，要设置成二维

#dp[i][j]表示从i到j是否是回文的，所以这个矩阵只有对角线右上部分才有意义（i要小于等于j）

#关系：当List[left] == List[right]时,若字符串长度只有1或者2，则dp[left][right] = 1
#                                    或dp[left + 1][right - 1] = 1时也等于1

def total_num(List):
    if List == []:
        return 0

    dp = [[0] * len(List) for _ in range(len(List))]
    total = 0
    for right in range(len(List)):
        for left in range(right):
            if List[right] == List[left] and (right - left < 2 or dp[left + 1][right - 1] == 1):   #找对关系很重要
                dp[left][right] =1
                total += 1

        dp[right][right] = 1
        total += 1

    return  total















