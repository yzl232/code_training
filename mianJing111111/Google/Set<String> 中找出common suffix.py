# encoding=utf-8
# Set<String> 中找出common suffix
#和prefix实际上是一致的。。
class Solution:
    # @return a string
    def longestCommonPrefix(self, arr):
        if not arr: return ''
        x = arr[0]
        for i in range(-1, -len(x)-1, -1):
            for s in arr[1:]:
                if len(s)<-i or s[i] !=x[i]:    return x[i+1:]
        return x