
#列表中最接近target的三个数之和,跟三数之和一个意思
def threeSumClosest(nums, target):
    nums.sort()
    output = nums[0]+nums[1]+nums[2]
    min_diff = abs(target - (nums[0] + nums[1] + nums[2]))

    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1

        while left < right:
            diff = abs(target - (nums[i] + nums[left] + nums[right]))
            if diff < min_diff:
                min_diff = diff
                output = nums[i] + nums[left] + nums[right]

            if target - (nums[i] + nums[left] + nums[right]) == 0:
                return nums[i] + nums[left] + nums[right]
            elif target - (nums[i] + nums[left] + nums[right]) > 0:
                left += 1
            else:
                right -= 1

    return output

if __name__ == '__main__':
    List = [0,2,1,-3]
    num = 1
    print(threeSumClosest(List, num))
