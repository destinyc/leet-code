
#举例 [1,7,2,8,3,4]的最长上升子序列是[1,2,3,4],长度是4

#动态规划的第一步是分解：长为n的List的结果和前n-1个元素的最长序列什么区别？
# max(n) = max(n - 1) + (第n个元素是否大于  前n-1个元素  最长序列的最后一个元素)

#重点是下面一句话
#这时要想明白一个东西 若dp[i] = num说明第i个元素前面有num-1个比他小的
#所以dp[i + 1]要判断这个新元素和前面所有dp做比较来找到最长的
#  dp[n] = max(dp[0]...dp[n-1]) + (List[n] > List[i])这个i从0到n-1

def caculate(List):
    if List == []:
        return 0

    dp = [0] * len(List)
    max_length = 1
    for i in range(len(List)):
        dp[i] = 1             #每一步都先初始化为1（代表本身元素是一个最长序列）

        for j in range(i):                              #遍历i之前的所有dp并与他们比较，这个循环结束后我们得到了dp[i]，即前面有几个元素比他小
            if List[i] > List[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
        max_length = max(max_length, dp[i])

    print(dp)
    return max_length


if __name__ == '__main__':
    List = [5,6,7,1,4,8]
    caculate(List)