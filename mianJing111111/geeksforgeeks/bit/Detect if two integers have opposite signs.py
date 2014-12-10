# encoding=utf-8
'''
detect if two integers have opposite signs

Given two signed integers, write a function that returns true if the signs of given integers are different, otherwise false.
'''
class Solution:
    def oppo(self, x, y):
        return (x^y) <0

s = Solution()
print s.oppo(5, -10)
print s.oppo(5, 8)

'''
bool oppositeSigns(int x, int y)
{
    return ((x ^ y) >> 31);
}
'''