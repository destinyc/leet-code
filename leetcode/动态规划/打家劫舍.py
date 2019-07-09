
#输入一个列表表示每家可以盗窃的金额，不能连续盗窃两家，求最大盗窃金额

#先找关系 money[0] = List[0]   money[1] = max(List[0],List[1])
# money[n] = max(money[n-1], money[n - 2] + List[n])

#最后返回最后一项

def thief_money(List):
    if List == []:
        return 0
    money = [0] * len(List)        #保存的是到这一家为止能盗窃的最高金额
    if len(List) == 1:
        return List[0]
    money[0], money[1] = List[0], max(List[0],List[1])
    for i in range(2, len(List)):
        money[i] = max(money[i-1], money[i-2] + List[i])

    return money[-1]



# 打家劫舍系列第二题：房屋的首尾相连是个环

# 我们把列表分成两部分： List[1:]  和 List[:-1]  两部分分开坐，就能保证了首尾不会同时被选到

#基本的动态规划过程还是不变的

def thief(List):
    if len(List) == 0:
        return 0
    if len(List) == 1:
        return List[-1]

    max_1, max_2 = thief_money(List[1:]), thief_money(List[:-1])

    return max(max_1, max_2)




if __name__ == '__main__':
    List = [1,2,3,1]
    # print(thief_money(List))
    print(thief(List))