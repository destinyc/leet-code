
#这道题可以找规律：
#位数为n+1的格雷码的前2**n个数是位数为n的格雷码最前面加个0，
# 后2**n个格雷码是位数为n的格雷码的逆序后在前面加1

def bianma(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        List = [0, 1]
        for i in range(2, n + 1):
            List = List + [2 ** (i - 1) + item for item in List[::-1]]

    return List

if __name__ == '__main__':
    n = 3
    print(bianma(n))