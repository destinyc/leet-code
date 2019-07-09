
#题目描述:
#  A = [a1, a2, a3...an], B = [b1, b2, b3...bn]
#已知A得到B使得 bi = a1*a2...ai-1*ai+1...an
#要求不能用除法

def caculate(A):
    B = [1] * len(A)

    for i in range(1, len(A)):
        B[i] = B[i - 1] * A[ i - 1]                  #这一步是吧每个bi的前半部分计算出来(即a1*a2...*ai-1)

    temp = 1
    for i in range(len(A) - 2, 0, -1):
        temp *= A[i + 1]                                 #这一步是在累积每个bi的后半部分
        B[i] *= temp

    return B


if __name__ == '__main__':
    A = [1,2,3,4,5,6]
    B = caculate(A)
    print(B)