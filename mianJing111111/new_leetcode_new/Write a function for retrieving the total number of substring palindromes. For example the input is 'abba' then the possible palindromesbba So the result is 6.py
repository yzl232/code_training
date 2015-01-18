# encoding=utf-8
'''
Write a function for retrieving the total number of substring palindromes.
For example the input is 'abba' then the possible palindromes= a, b, b, a, bb, abba
So the result is 6.

Updated at 11/11/2013:
After the interview I got know that the O(n^3) solution is not enough to go to the next round. It would have been better to know before starting implementing the solution unnecessarily ...
暴力方法可以提。 但是不要写。


和  longest  palindrome   leetcode 类似的题目。




  艹。  O(n)的也要背下来。  dp.  以及O(n2) 三种都要。

'''

class Solution:
    # @return a string    O(n2)  #space 用太多。 效率其实不好
    def longestPalindrome(self, s):  # http://blog.csdn.net/feliciafay/article/details/16984031
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        num = 0
        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j] and (j-i<=1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    num+=1
        return  num#如出一辙 https://oj.leetcode.com/submissions/detail/13147843/



#下面这个经典的O(n). 背下
class Solution11:
    # @return a string
    def longestPalindrome(self, s):  # http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
        T = self.process(s)
        C = 0  # central point
        R = 0  # the boundry point of the maximum palindrome.  C+P[C]
        P = [0 for i in range(len(T))]
        for i in range(1, len(T)-1):
            i_mirror = 2*C - i
            P[i] = min(R-i, P[i_mirror]) if R>i else 0     #min(R-i,
            while T[i+1+P[i]] == T[i-1-P[i]]:  # // Attempt to expand palindrome centered at i
                P[i] = P[i] + 1
            #If palindrome centered at i expand past R,   adjust center based on expanded palindrome.
            if i+P[i] > R:
                C = i
                R = i + P[i]
        return sum((i+1)/2 for i in P) #经过测验   一个substring如果是palindrome。 以之为中心的为(i+1)/2个一个substring如果是palindrome

    def process(self, s):
        ret = '^'
        for i in range(0, len(s)):
            ret += '#'+s[i]
        ret +='#$'
        return ret
a = Solution11()
print a.longestPalindrome("aaa") #确实6个
print a.longestPalindrome("abcd")
print a.longestPalindrome("abba")


#背下代码。 和一个例子就好
#abba
'''
^ a # b # b # a$
0 1  0 1 4 1 0 1 0
'''


class Solution6:  # O(1) space  O(n2)
    # @return a string
    def expand(self, s, l, r):
        cout = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:  #这里设定好了边界
            l -= 1; r += 1
            cout+=1
        return cout

    def longestPalindrome(self, s):
        return sum(self.expand(s, i, i)+self.expand(s, i, i+1) for i in range(len(s)))


sss = Solution6()
print sss.longestPalindrome('abba')