# encoding=utf-8
'''
给你5个空_ _ _ _ _, 每次猜一个字母，这里出题人想让你猜出来clock，假如你猜a，告诉你这里面没有。你又猜c，他把c全写出来，所以你有c _ _ c _。 让你最多猜10次。写一个程序去猜。输入是几个空，要考虑每次猜的反馈，尽量把词猜出来
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

    def play(self, n=10):
        while True:
            if n==0: print "you lose the game"
            x = raw_input(''.join(self.cur)+"\n")
            if x in self.d:
                for i in self.d[x]:
                    self.cur[i]=self.word[i]
            if self.word==self.cur:
                print ''.join(self.word)
                print "you win the game"
                break

s = Game("banana")
s.play()
