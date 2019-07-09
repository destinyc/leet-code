
#直接扩展输出
def find(List):
    output = ''
    if List == []:
        return output
    S = List[0]

    for i, s in enumerate(S):
        index = 1
        while index < len(List):
            if i < len(List[index]):
                if List[index][i] != s:
                    return output
            else:
                return output
            index += 1

        output += s

    return output

#方法2
def _find(List):
    if len(List) == 0:
        return ''

    List.sort(key=lambda i: len(i))
    min_str = List[0]

    while min_str:
        i = 0
        for s in List[1:]:
            if min_str in s[:len(min_str)]:
                i += 1

        if i == len(List) - 1:
            break
        else:
            min_str = min_str[:len(min_str) - 1]             #将最短的字符串去除末尾的字符

    return min_str

if __name__ == '__main__':
    List = ["dog","racecar","car"]
    print(find(List))


