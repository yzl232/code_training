# encoding=utf-8
'''
给你5个空_ _ _ _ _, 每次猜一个字母，这里出题人想让你猜出来clock，假如你猜a，告诉你这里面没有。你又猜c，他把c全写出来，所以你有c _ _ c _。 让你最多猜10次。写一个程序去猜。输入是几个空，要考虑每次猜的反馈，尽量把词猜出来
'''

#如何能够最大化猜对的几率.
'''
实现一个hangman游戏，给定一个词作为答案，然后进行猜测。猜测的时候只知道这个词的长度。每次可以从26个字母里的猜一个字母，如果该单词存在该字母，这些字母都会明确出在单词中的位置，并且可以进行下一轮猜测，否则算错。如果一共错了六次就不能再猜了。如何能够最大化猜对的几率。例如答案为hangman，一开始的字符串为"*******"，如果猜n，正确，可以显现"**n***n"，再猜a，正确，可以显现"*an**an"。
我用的DFS，按照字典里   字母出现频率由高往低去猜(元音要高一些)。
'''


#用hashmap。 比较傲简单。

class Game:
    def __init__(self, word):
        self.word = list(word)
        self.d = self.cnt(word)
        self.cur = ['_']*len(word)

    def cnt(self, word):
        d = {}
        for i in range(len(word)):
            ch = word[i]
            if ch not in d: d[ch]=[]
            d[ch].append(i)
        return d

    def play(self, n=5):
        while True:
            if n==0:
                print "you lose the game"
                break
            x = raw_input(''.join(self.cur)+"\n")
            if x in self.d:
                for i in self.d[x]:
                    self.cur[i]=self.word[i]
            if self.word==self.cur:
                print ''.join(self.word)
                print "you win the game"
                break
            n-=1

s = Game("banana")
s.play()
