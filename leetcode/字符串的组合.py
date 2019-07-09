
def combination(List):
    if len(List) == 0:
        return []

    output = []

    for i in range(1, len(List)):            #选择的字符的个数
        zuhe(List, output, i, [])

    # print(output)


def zuhe(List, output, num, path):
    if num == 0:
        output.append(path)
        print(path)

    if len(List) == 0:
        return

    else:
        path.append(List[0])
        zuhe(List[1:], output, num - 1, path)           #选择了List的第一个元素，并递归从剩下的元素中选出来 num-1个元素

        path.pop()
        zuhe(List[1:], output, num, path)               #不要第一个元素，那就要从剩下的元素中选num个

if __name__ == '__main__':
    List = ['a', 'b', 'c']
    combination(List)

