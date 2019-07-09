
#从0到n-1组成圈，从0开始，每隔m个数删一个，最后剩下谁
#普通解法
def find(n, m):
    if n == 1:
        return 1

    List = [i for i in range(n)]
    index = 0
    while len(List) > 1:
        index = (m + index - 1) % len(List)
        List.pop(index)

    return List[0]

#创新解法，找规律
def _find(n, m):
    if n == 1:
        return 1
    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i

    return last

if __name__ == '__main__':
    n, m = 7, 3
    print(find(n, m))