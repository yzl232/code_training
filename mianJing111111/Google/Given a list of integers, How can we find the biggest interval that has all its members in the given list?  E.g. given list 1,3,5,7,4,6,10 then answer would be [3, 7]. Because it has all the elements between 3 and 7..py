# encoding=utf-8
'''
Given a list of integers, How can we find the biggest interval that has all its members in the given list?

E.g. given list 1,3,5,7,4,6,10 then answer would be [3, 7]. Because it has all the elements between 3 and 7.

O(n)
'''

#居然是leetcode原题。
#leetcode longest consecutive sequence. 区别在于leetcode求长度。 这个返回具体的区间。



class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        d = {x:False for x in num} # False means not visited
        ret = (0, 0)
        for i in d:
            if not d[i]:
                a = i + 1;  b = i - 1
                while a in d and not d[a]:
                    d[a] = True; a += 1
                while b in d and not d[b]:
                    d[b] = True; b -= 1
                if (a-b-1)>ret[1]-ret[0]+1:  ret = (b, a)  #
        return ret