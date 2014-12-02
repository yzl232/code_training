# encoding=utf-8
class Solution:
    def swap(self, x, y):
        x ^=y
        y ^=x   #背下。 不难理解。   消去y，留下x
        x ^=y  #消去x，留下y
        return x, y

s = Solution()
print s.swap(5, 7)