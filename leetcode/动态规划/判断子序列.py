
#不需要连续，但每个字符的前后顺序还是要保持的

#我这个思路好像不是动态规划，但是效果挺不错的
#可以用双指针，一个指针指向s的当前元素，另一个指针指向t的当前元素，不匹配时t递增，匹配时两个都递增

def isSubsequence(s, t):
    if len(s) == 0:
        return True

    index = -1
    for char in s:
        if char not in t[index + 1:]:
            return False

        index = t[index + 1:].index(char) + index + 1

    return True

if __name__ == '__main__':
    s = "acc"
    t = "ahbgdc"

    print(isSubsequence(s, t))