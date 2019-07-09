
#变相考察二分查找

class Solution:
    def __init__(self):
        pass
    def count(self, nums, mid):
        n = len(nums)
        j = count = 0

        #for循环计算对于每个数存在多少个数和他的距离小于mid，最后全部加起来就是总的小于mid的数目

        for i in range(n - 1):            #n维持的是左侧指针
            while j < n and nums[j] - nums[i] <= mid:            #j维护的是右侧指针
                j += 1
            count = count + j - i - 1

        return count

    def smallestDistancePair(self, nums, k):
        nums.sort()
        low, high = 0, nums[-1] - nums[0]           #现将数组排序，然后设置最大和最小距离

        while low < high:
            mid = low + (high - low) // 2
            count = self.count(nums, mid)           #找到中间距离，然后计算小于中间距离的个数

            if count < k:                           #说明中间距离比第k个距离小，那么区间就是后一半
                low = mid + 1
            else:
                high = mid
        return low

if __name__ == '__main__':
    List = [1,3,1]
    k = 1

    C = Solution()
    print(C.smallestDistancePair(List, k))





