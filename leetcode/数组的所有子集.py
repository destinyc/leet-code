
def find(List):
    if List == []:
        return []
    output = [[]]
    for num in List:
        tmp = []
        for l in output:
            tmp.append(l + [num])              #关键是搞懂这句话的工作原理

        output.extend(tmp)

    return output

if __name__ == '__main__':
    List = [1, 2, 3]
    print(find(List))