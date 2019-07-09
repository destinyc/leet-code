
#先写一个简单的问题，判断一个数是否是丑数（只包含因子2，3，5）leetcode263

def isuglynum(num):
    if num == 1:
        return True
    if num == 0:
        return False

    while num % 2 == 0:
        num = num // 2

    while num % 3 == 0:
        num = num // 3

    while num % 5 == 0:
        num = num // 5

    if num == 1:
        return True
    return False


#找第n个丑数   leetcode264

#基本思路，我们从小到大只找丑数
def UglyNum(n):
    if n == 1:
        return 1

    current_num = [1] * n            #因为有n个丑数，我们先初始化一个数组
    next_index = 1                   #这是我们下一个要找的丑数

    Multiply2_index = 0
    Multiply3_index = 0
    Multiply5_index = 0              #我们时刻维护三个索引，这三个索引对应的是乘上相应因子后大于当前丑数的那个索引

    while next_index < n:
        current_num[next_index] = min(current_num[Multiply2_index] * 2,   #这三个数都是刚好比上一个丑数打，但我们要最小的那个
                                      current_num[Multiply3_index] * 3,
                                      current_num[Multiply5_index] * 5)


        #现在由于我们又找到了一个最新的最大丑数，所以相应的也要更新这三个索引的位置
        while current_num[Multiply2_index] * 2 <= current_num[next_index]:
            Multiply2_index += 1

        while current_num[Multiply3_index] * 3 <= current_num[next_index]:
            Multiply3_index += 1

        while current_num[Multiply5_index] * 5 <= current_num[next_index]:
            Multiply5_index += 1

        next_index += 1

    return current_num[-1]

if __name__ == '__main__':
    num = 10
    print(UglyNum(num))












