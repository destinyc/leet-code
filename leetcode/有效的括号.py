
def judgement(S):          #输入是括号的字符串
    dic = {'(' : ')', '{' :'}', '[' : ']'}
    zuokuohao = ['(', '[', '{']

    stack = []
    for s in S:
        if s in zuokuohao:
            stack.append(dic[s])
        else:
            if stack != []:
                s_ = stack.pop()
                if s != s_:
                    return False
            else:
                return False
    if stack == []:
        return True
    return False


if __name__ == '__main__':
    S = '()[(])()'
    print(judgement(S))