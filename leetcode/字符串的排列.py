
def permutation(s, output, path):
    if s == '':                    #递归结束的条件
        output.append(path)

    else:
        for i in range(len(s)):
            permutation(s[:i] + s[i+1 : ], output, path + [s[i]])      #相当于我们从s中选择一个放到这个位置，剩下的继续递归




def Permutation(s):         #核心知识点  全排列算法
    if s == '':
        return []
    output = []
    permutation(s, output, [])

    print(output)

if __name__ == '__main__':
    s = 'abc'
    Permutation(s)