
#两数之和,返回两个数的索引,使用字典做
def find(List, add):
    if List == []:
        return None
    dic = {}
    for index, num in enumerate(List):
        diff = add - num
        if diff in dic:
            return [dic[diff], index]
        dic[num] = index

#三数之和
def _find(List, add):          #注意数组中可以存在重复元素
    List.sort()              #毫无疑问，先排序
    if List == []:
        return None

    output = []

    for i in range(len(List)):                #先固定住一个数，然后找另外两个数
        if i == 0 or List[i] > List[i - 1]:      #可以跳过重复元素
            left = i + 1
            right = len(List) - 1                #维护另外两个数的指针

            while left < right:
                current_add = List[i] + List[left] + List[right]
                if current_add == add:
                    output.append([List[i], List[left], List[right]])

                    left += 1
                    right -= 1            #因为答案不能重复，所以这两个数不能再用了,要移动

                    while left < right and List[right] == List[right + 1]:         #跳过重复的答案
                        right -= 1
                    while left < right and List[left] == List[left - 1]:
                        left += 1

                elif current_add > add :
                    right -= 1
                    while left < right and List[right] == List[right + 1]:         #跳过重复的非答案
                        right -= 1

                else:
                    left += 1
                    while left < right and List[left] == List[left - 1]:
                        left += 1
    return output


#四数之和(之前想过先set来剔除重复，但是仔细想想不行，因为四个数中可能用到两个相等的数)
def _find_(List, add):              #同样元素存在重复
    if List == []:
        return None

    List.sort()
    output = []
    i = 0
    while i < len(List):        #第一个数的索引
        j = i + 1
        # while j < len(List) - 1 and List[j] == List[i]:     #不能跳过
        #     j += 1                                                     #举例 [0,0,0,0] add = 0跳过会出错

        while j < len(List):              #第二个数的索引

            left, right = j + 1, len(List) - 1          #维护剩下两个数的指针

            while left < right:
                current_add = List[i] + List[j] + List[left] + List[right]
                if current_add == add:
                    output.append([List[i], List[j], List[left], List[right]])
                    left += 1
                    right -= 1

                    while left < right and List[right] == List[right + 1]:        #跳过重复答案
                        right -= 1
                    while left < right and List[left] == List[left - 1]:
                        left += 1

                elif current_add > add:
                    right -= 1
                    while left < right and List[right] == List[right + 1]:         #跳过重复的错误答案
                        right -= 1
                else:
                    left += 1
                    while left < right and List[left] == List[left - 1]:
                        left += 1

            j += 1                                                #跳过第二个数的重复
            while j < len(List) and List[j] == List[j - 1]:
                j += 1

        i += 1
        while i < len(List) and List[i] == List[i - 1]:
            i += 1

    return output








if __name__ == '__main__':
    List = [-3,-2,-1,0,0,1,2,3]
    add = 0
    print(_find_(List, add))