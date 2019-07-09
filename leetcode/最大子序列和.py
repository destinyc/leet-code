
def maxSum(List):
    if List == []:
        return 0

    maxSum = List[0]

    for num in List[1:]:
        current_sum = maxSum + num
        if current_sum > maxSum:
            maxSum = current_sum

        if current_sum < 0:         #当前加上的是个负数，且比前面这么多次的累加还要小，就抛弃前面所有的，从下个数开始重新算
            maxSum = 0

    return maxSum