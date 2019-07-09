
#这个函数只能转换整数  leetcode 8
def convert(s):
    s.strip()

    if s == '':
        return 0
    index = 0
    output = ''
    fuhao = '+'
    if [index] == '+' or s[index] == '-':
        fuhao = s[index]
        index += 1
        if index == len(s):
            return 0

    while index < len(s):
        if '0' <= s[index] <= '9':
            output += s[index]

        else:
            break

    if fuhao == '-':
        return -1 * int(output)
    else:
        return int(output)

#判断一个字符串能否表示数值,剑指offer

def judgement(s):
    s.strip()
    if s == '':
        return False
    index = 0
    if s[index] == '+' or s[index] == '-':
        index += 1
        if index == len(s):                       #只有一个符号
            return False

    while index < len(s):
        




























