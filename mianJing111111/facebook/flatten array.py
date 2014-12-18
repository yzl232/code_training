# encoding=utf-8
'''

'''
class Solution:
    def flatten(self, arr):
        ret = []
        for i in arr:
            if isinstance(i, list):    ret+=self.flatten(i)
            else:  ret.append(i)
        return ret
s = Solution()
print s.flatten( [ [1,2], [3,[4,5]], 6])