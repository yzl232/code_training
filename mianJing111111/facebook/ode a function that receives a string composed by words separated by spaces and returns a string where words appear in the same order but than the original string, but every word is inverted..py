# encoding=utf-8
'''
和leetcode不一样。我傻了。。

Code a function that receives a string composed by words separated by spaces and returns a string where words appear in the same order but than the original string, but every word is inverted.
Example, for this input string

@"the boy ran"

the output would be

@"eht yob nar"

Tell the complexity of the solution.
'''
class Solution:
    def re(self, s):
        words = s.split()
        for i in len(words):
            words[i].reverse()
        return ' '.join(words)


class Solution3:
    def reverseWords(self, charArr):
        start=j=0  #比leetcode少了一步
        while j<=len(charArr)-1:
            if  charArr[j] == ' ':
                self.reverse(charArr, start, j-1)
                start = j+1
            j+=1
        return charArr

    def reverse(self, charArr, begin, end):
        while begin<end:
            charArr[begin], charArr[end] = charArr[end], charArr[begin]
            begin+=1;  end-=1



# leetcode in place 做法
class Solution3:
    def reverseWords(self, charArr):
        self.reverse(charArr, 0, len(charArr)-1)
        print charArr
        start=j=0
        while j<=len(charArr)-1:
            if  charArr[j] == ' ':
                self.reverse(charArr, start, j-1)
                start = j+1
            j+=1

        return charArr

    def reverse(self, charArr, begin, end):
        while begin<end:
            charArr[begin], charArr[end] = charArr[end], charArr[begin]
            begin+=1;  end-=1

s = Solution()
print s.reverseWords(list('the sky is blue'))