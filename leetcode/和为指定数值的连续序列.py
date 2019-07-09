
#我们找的是从1开始，所有的能让和等于k的连续序列
#例如： k = 14 输出序列1到5、4到6、7到8
def find(k):
    #             和刚刚的两数之和一样，我们用两个指针表示序列的最大数和最小数,但是只有k大于三时才能这样处理
    if k == 0:
        return None
    if k == 1:
        return [1]
    if k == 2:
        return [2]

    output = []
    begin, end = 1, 2

    mid = (1 + k) // 2               #这是一个用于循环的基准，begin不可能大于它
    current_sum = begin + end

    while begin < mid:
        if current_sum == k:
            output.append([i for i in range(begin, end + 1)])

        while current_sum > k and begin < mid:                   #序列的和太大，从头部开始缩小序列，直到小于等于k
            current_sum -= begin
            begin += 1

            if current_sum == k:
                output.append([i for i in range(begin, end + 1)])

        end += 1
        current_sum += end                #现在已经小于等于k了，扩展尾部继续向后走


