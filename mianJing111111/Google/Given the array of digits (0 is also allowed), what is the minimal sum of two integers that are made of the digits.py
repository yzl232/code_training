# encoding=utf-8
'''
Given the array of digits (0 is also allowed), what is the minimal sum of two integers that are made of the digits contained in the array.
For example, array: 1 2 7 8 9. The min sum (129 + 78) should be 207
'''

'''
Sort the array. The largest numbers should be in the least significant positions, so build up your two integers by alternating from the two arrays.
E.g. 1 3 5 7 8 9 => 1 and 3, then 15 and 37, then 158 and 379. 0 is a special case, if not allowed to use that as a leading digit then have to use it as the second digit.
'''

# 先sort。 用counting sort
#然后alternative 分为 2个部分。
#得问清楚0可不可以在第一位。 比如045
#先假设0可以在首位
class Solution:
    def minSum(self, arr):
        if not arr: return 0
        arr = [str(i) for i in sorted(arr)]
        one =int( ''.join(arr[i] for i in range(0, len(arr), 2)) )
        two =int( ''.join(arr[i] for i in range(1, len(arr), 2)) )
        return one+two