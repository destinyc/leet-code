
#leetcode79   和  leetcode212两个版本

#leetcode79, 二维网格，只能搜索相邻元素，不能重复使用        DFS搜索
def search(List, word):
    if word == '':
        return True
    if len(List) == 0:
        return False

    columns, rows = len(List), len(List[0])

    for column in range(columns):
        for row in range(rows):
            if isFound(List, word, column, row):          #从这个位置出发能否得到单词
                return True

    return False


def isFound(List, word, column, row):
    if word == '':            #已经把单词查找完了，成功走到了最后
        return True

    if column < 0 or row < 0 or column >= len(List) or row >= len(List[0]) \
                  or List[column][row] != word[0]:         #当前网格不等于单词的当前字符（自动包含了已经走过这个格子的情况）
        return False

    current_str = List[column][row]                #记录下当前网格的字符，若此路不通我们还要把他还原回来
    List[column][row] = '.'                        #表示走过这里了

    if isFound(List, word[1:], column - 1, row) \
           or isFound(List, word[1:], column + 1, row) \
           or isFound(List, word[1:], column, row - 1) \
           or isFound(List, word[1:], column, row + 1):              #开始递归

        return True

    List[column][row] = current_str                  #没有走通这条路，就把字符还原回来
    return False


#leetcode212  没啥大的变化，就是这次给了个单词的列表，找出所有在网格中的单词
# 可以对列表中所有单词做一个判断，也能通过，只是不是最好做法（无所谓了。。）

#但是要注意一点，上面的题，由于只有一个单词，所以如果走通了，走过的路径我们就不还原直接输出了True
#  而现在有多个单词，所以不管当前单词即使走通了，也要把List改回来才能走下一个单词

class Solution:
    def isFound(self, List, word, column, row):
        if word == '':
            return True

        if column < 0 or row < 0 or column >= len(List) or row >= len(List[0]) \
                or List[column][row] != word[0]:  # 当前网格不等于单词的当前字符（自动包含了已经走过这个格子的情况）
            return False

        current_str = List[column][row]  # 记录下当前网格的字符，若此路不通我们还要把他还原回来
        List[column][row] = '.'  # 表示走过这里了

        if self.isFound(List, word[1:], column - 1, row) \
                or self.isFound(List, word[1:], column + 1, row) \
                or self.isFound(List, word[1:], column, row - 1) \
                or self.isFound(List, word[1:], column, row + 1):  # 开始递归

            return True

        List[column][row] = current_str  # 没有走通这条路，就把字符还原回来
        return False

    def findWords(self, List, words):
        output = []
        if len(words) == 0 or len(List) == 0:
            return output

        columns, rows = len(List), len(List[0])

        for word in words:
            board = [[item for item in column] for column in List]        #每重新检测一个单词，我们传入的都只是List的副本
            for column in range(columns):                                 #由此来还原上个单词走过后的List
                for row in range(rows):
                    if self.isFound(board, word, column, row):
                        output.append(word)

        return output



if __name__ == '__main__':
    List = [['a']]
    word = 'b'
    # print(search(List, word))



    # List = [
    #     ['o', 'a', 'a', 'n'],
    #     ['e', 't', 'a', 'e'],
    #     ['i', 'h', 'k', 'r'],
    #     ['i', 'f', 'l', 'v']
    # ]
    # words = ["oath","pea","eat","rain"]
    words = ['b']
    solu = Solution()
    print(solu.findWords(List, words))

















