
def find(List):

    #原理：我们从头开始，若元素与当前元素一样，times就加一，否则减一，最后的元素就是要找的元素

    if len(List) == None:
        return None

    times = 1
    result = List[0]
    for index in range(1, len(List)):
        if times == 0:
            times = 1
            result = List[index]
        else:
            if List[index] == result:
                times += 1
            else:
                times -= 1

    return result

if __name__ == '__main__':
    List = [6,5,5]
    print(find(List))
