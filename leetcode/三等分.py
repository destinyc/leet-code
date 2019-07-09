
class Solution:

    def threeEqualParts(self, A):
        total = A.count(1)
        length = len(A)

        if not total:
            return [0, length - 1]
        if total % 3 != 0:
            return [-1, -1]
        step = total // 3

        p, cnt = [0] * 3, 0         #p中存放的是第一个1的坐标，第step+1个1的坐标，第2*step+1的坐标
        for i, num in enumerate(A):
            if num == 1:
                if cnt % step == 0:
                    p[cnt // step] = i
                cnt += 1

        while p[2] < length and A[p[0]] == A[p[1]] and A[p[1]] == A[p[2]]:
            p[0] += 1
            p[1] += 1
            p[2] += 1

        if p[2] == length:                    #要想明白一件事，三段相等的话，第三段的长度一定是最短的。
            return [p[0] - 1, p[1]]

        return [-1, -1]





if __name__ == '__main__':
    A = [1,0,1,0,1]
    C = Solution()
    r = C.threeEqualParts(A)
    print(r)