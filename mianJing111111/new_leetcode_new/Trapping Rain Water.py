# encoding=utf-8
'''
Trapping Rain Water

面试中见到lc 原题并不奇怪，而面试官在原题基础上给你一个此题的follow up也并不新鲜， 这个题的一个follow up是若某一个bar的高度是0， 代表这个bar漏水， 不能存水， 那你的代码该如何改动去计算储水量？
面试官只是想吓唬你，看你应变能力，根本就是同一个题。 在计算left 和right 时，判断一下 A是否为0， 若为0， 也为0 便是...

'''


'''
Trapping Rain Water

面试中见到lc 原题并不奇怪，而面试官在原题基础上给你一个此题的follow up也并不新鲜， 这个题的一个follow up是若某一个bar的高度是0， 代表这个bar漏水， 不能存水， 那你的代码该如何改动去计算储水量？
面试官只是想吓唬你，看你应变能力，根本就是同一个题。 在计算left 和right 时，判断一下 A是否为0， 若为0， 也为0 便是...

'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, arr): # http://yucoding.blogspot.com/2013/05/leetcode-question-111-trapping-rain.html
        n = len(arr); ret = 0
        l = [0 for i in range(n)];  r =l[:]
        for i in range(1, n-1):    l[i] = max(l[i-1], arr[i-1]) if arr[i] else 0
        for i in range(n-2, 0, -1):    r[i] = max(r[i+1], arr[i+1]) if arr[i] else 0
        for i in range(1, n-1):  ret += max(  min(l[i], r[i])-arr[i],   0)
        return ret





'''


下面是leetcode原来的代码
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, arr): # http://yucoding.blogspot.com/2013/05/leetcode-question-111-trapping-rain.html
        n = len(arr); ret = 0
        l = [0 for i in range(n)];  r =l[:]
        for i in range(1, n-1):    l[i] = max(l[i-1], arr[i-1])
        for i in range(n-2, 0, -1):    r[i] = max(r[i+1], arr[i+1])
        for i in range(1, n-1):  ret += max(  min(l[i], r[i])-arr[i],   0)
        return ret

