class Solution:
    # @return a list of integers
    def grayCode(self, n):
        return [(i>>1)^i for i in range(2**n)]