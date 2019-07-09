#举例
#[3, 32, 321]组成的最小数 321323

def compare(num1, num2):         #在这里我们比较两个数的两种拼接方法哪个小
    s1 = str(num1) + str(num2)
    s1 = int(s1)

    s2 = str(num2) + str(num1)
    s2 = int(s2)

    return s1 > s2


def min_num(List):
    if List == []:
        return 0

    for i in range(len(List)):
        List[i] = str(List[i])

    import functools
    List.sort(key = functools.cmp_to_key(compare))             #使用自己定义的compare函数进行排序

    output = ''
    for item in List:
        output += item

    return int(output)

if __name__ == '__main__':
    List = [321, 32, 3]

    print(min_num(List))


