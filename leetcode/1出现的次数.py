
def countDigitOne(num):
    if num < 0:
        return 0
    s = str(num)
    output = numberOf1(s)

    return output

def numberOf1(s):             #输入的是数字编程的字符串，处理每一个位比较方便
    first = int(s[0])        #先把最高位取出来

    if len(s) == 1 and first == 0:    #数是0
        return 0
    if len(s) == 1 and first > 0:     #数是1到9
        return 1

    #先计算最高位的1的个数:
    first_count = 0
    if first_count == 1:
        first_count = int(s[1:]) + 1              #这里以1345为例，最高位1的个数是356个(从1000到1345的高位是1)
    if first > 1:
        first_count = 10 ** (len(s) - 1)         #这里以2345为例，最高位1的个数是1000个（从1000到1999的高位都是1）

    #如果输入的是4位数，这一步计算的是3位数1的个数和4位数中初最高位外1的个数（即从345到2345中其它三位出现的1的次数）
    other_count = first * (len(s) - 1) * (10 ** (len(s) - 2))     #即每一位都可能是1，其它位是0到9

    #递归计算(计算1到345出现的1的次数)
    recursive_num = numberOf1(s[1:])

    return first_count + other_count + recursive_num















