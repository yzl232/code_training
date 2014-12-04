# encoding=utf-8
'''

'''
class Solution:
    def flatten(self, arr):
        result = []
        for i in arr:
            if isinstance(i, list):
                result+=self.flatten(i)
            else:  result.append(i)
        return result
s = Solution()
print s.flatten( [ [1,2], [3,[4,5]], 6])