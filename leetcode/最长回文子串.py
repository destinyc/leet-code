
#暴力查找法：容易超出时间限制
def search(S):
    if S == S[::-1]:
        return S

    output = ''
    for left in range(len(S)):
        for right in range(left, len(S)):
            if S[left : right + 1] == S[left : right + 1][::-1] and len(S[left : right + 1]) > len(output):
                output = S[left : right + 1]

    return output


#马拉车算法，专门用来做这道题的算法
def _search(S):
    if S == S[::-1]:
        return S