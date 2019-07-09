
#给定一个列表，返回最大的容器的两个数值存放的水量

#暴力求解法不再写，这里使用双指针法
#这里要明白一件事，两个柱子中间存的水量是由短的那根柱子决定的，当短柱子确定下来后，另一根柱子当然是越远越好
def maxArea(List):
    pointer1, pointer2 = 0, len(List) - 1
    maxArea = 0
    while pointer1 < pointer2:
        maxArea = max(maxArea, min(List[pointer1], List[pointer2]) * (pointer2 - pointer1))

        if List[pointer1] < List[pointer2]:       #因为我们的两个指针在不断向中间靠拢，所以要想面积增大，就只能抛弃短的那根
            pointer1 += 1
        else:
            pointer2 -= 1

    return maxArea

if __name__ == '__main__':
    List = [1,8,6,2,5,4,8,3,7]
    print(maxArea(List))