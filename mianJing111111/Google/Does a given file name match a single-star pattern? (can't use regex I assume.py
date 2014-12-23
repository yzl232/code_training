# encoding=utf-8
'''
Does a given file name match a single-star pattern? (can't use regex I assume)
index.html matches *.html
foo.txt does not match *.html

matches(“index.html”, “*html”) returns true
matches(“foo.txt”, “*html”) returns false
matches(“cat”, “c*t”) returns true
'''


# wild card matching
class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    #http://blog.csdn.net/lifajun90/article/details/10582733
    #http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
    def isMatch(self, s, p):
        m = len(s) ; n = len(p)
        j = i = match = 0; star = -1 #i==pPointer.  j==sPointer
        while i < m:
            if j < n and p[j] == '*':
                star = j; j +=1; match = i;
            elif j < n and (p[j] in ('?', s[i]) ):
                i+=1; j +=1
            elif star != -1:  # not match, 逐个增加*适配的范围。 看看结果
                j = star + 1; match+=1; i = match
            else:   return False
        while j < n and p[j] == '*':   j +=1
        return  j == n