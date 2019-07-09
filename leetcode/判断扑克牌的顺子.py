
def jugment(List):
    List.sort()

    numOfzero = List.count(0)

    for i in range(numOfzero + 1, len(List)):

        diff = List[i] - List[i - 1]
        if diff == 0:         #扑克牌中存在对儿
            return False
        elif diff == 1:
            continue
        else:
            if diff > numOfzero + 1:
                return False
            else:
                numOfzero -= diff
    return True


if __name__ == '__main__':
    List = [0,2,3,5,6,7,7]

    print(jugment(List))

