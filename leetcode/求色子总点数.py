
#递归求解，每次固定一个色子

def caculate(number):                #输入的是色子的个数
    if number < 1:
        return 0

    max_num = number * 6              #最大的可能点数,最小点数是number

    show_times = [0] * (max_num - number + 1)    #对应的点数存在下标 num - number位置

    for i in range(1, 7):
        digui(number, number, i, show_times)

    return show_times


def digui(original_number, current_number, sum, show_times):
    if current_number == 1:                        #已经递归过所有色子了
        show_times[sum - original_number] += 1

    else:
        for i in range(1, 7):
            digui(original_number, current_number - 1, sum + i, show_times)


if __name__ == '__main__':
    number = 1
    show_times = caculate(number)
    print(show_times)