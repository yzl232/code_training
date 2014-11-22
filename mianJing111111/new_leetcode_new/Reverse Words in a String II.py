# encoding=utf-8
'''
Reverse Words in a String II

given s = "the sky is blue", return "blue is sky the".

Similar to Question [6. Reverse Words in a String], but with the following constraints:
“The input string does not contain leading or trailing spaces and the words are always separated by a single space.”
Could you do it in-place without allocating extra space?


This can be done without any additional space in 2 pass
1) reverse the string in place
2) reverse each word of the reversed string.

'''
class Solution:
    def reverseWords(self, charArr):
        self.reverse(charArr, 0, len(charArr)-1)
        print charArr
        i=j=0
        while j<=len(charArr)-1:
            if  charArr[j] == ' ':
                self.reverse(charArr, i, j-1)
                i = j+1
            j+=1

        return charArr

    def reverse(self, charArr, begin, end):
        while begin<end:
            charArr[begin], charArr[end] = charArr[end], charArr[begin]
            begin+=1;  end-=1

s = Solution()
print s.reverseWords(list('the sky is blue'))