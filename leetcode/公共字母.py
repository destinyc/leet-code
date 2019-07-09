
def commonChars(A):
    L = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    nums_list = [[] for i in range(len(A))]
    for i in range(len(A)):
        for char in L:
            nums_list[i].append(A[i].count(char))

    output = []
    for i in range(len(L)):
        char_num = min([l[i] for l in nums_list])
        if char_num > 0:
            for _ in range(char_num):
                output.append(L[i])

    return output

if __name__ == '__main__':
    A = ["cool","lock","cook"]
    output = commonChars(A)
    print(output)






