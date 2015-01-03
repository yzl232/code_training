# encoding=utf-8
# Set<String> 中找出common suffix
#和prefix实际上是一致的。
class Solution:
    # @return a string
    def longestCommonPrefix(self, strsArr):
        if not strsArr: return ''
        for i in range(-1, -len(strsArr[0])-1, -1):
            for j in range(1, len(strsArr)):
                if len(strsArr[j])<abs(i) or strsArr[j][i] != strsArr[0][i]:    return strsArr[0][:i]
        return strsArr[0]