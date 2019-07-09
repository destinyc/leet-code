
#第一版本，leetcode496
#给出两个list，其中一个是另一个的子集，返回这个子集列表元素在大列表中的下一个更大元素或-1

def find_next(nums1, nums2):        #双循环暴力
    output = []
    for num in nums1:
        index = nums2.index(num) + 1
        while index < len(nums2):
            if nums2[index] > num:
                output.append(nums2[index])
                break
            index += 1
        if index == len(nums2):
            output.append(-1)

    return output


#第二版，输入一个列表（首尾相连的），找到每个元素的下一个更大元素，没有则返回-1

#使用单调递减stack存储元素的index

def _find_next(nums):
    if nums == []:
        return []
    stack, output = [], [-1]*len(nums)

    for index in range(len(nums)):
        while stack and nums[stack[-1]] < nums[index]:    #stack.pop()索引对应的下一个更大元素都是 nums[index]
            output[stack.pop()] = nums[index]

        stack.append(index)

    #由于是环形列表，元素的下一个最大值可能在前面，所以再循环一次
    for index in range(len(nums)):
        while stack and nums[stack[-1]] < nums[index]:
            output[stack.pop()] = nums[index]

        stack.append(index)

    return output
