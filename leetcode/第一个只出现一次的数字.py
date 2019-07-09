

def firstUniqChar(s):
    if s == '':
        return -1

    dic = {}                          #使用字典存储字符出现次数
    for s_ in s:
        if s_ in dic:
            dic[s_] += 1
        else:
            dic[s_] = 1

    for index, s_ in enumerate(s):   #第二次便利找第一个出现一次的字符(或数字)
        if dic[s_] == 1:
            return index

    return -1
