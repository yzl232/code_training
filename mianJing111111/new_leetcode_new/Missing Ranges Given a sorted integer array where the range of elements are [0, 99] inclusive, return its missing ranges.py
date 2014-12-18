# encoding=utf-8
'''
Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]
Example Questions Candidate Might Ask:
Q: What if the given array is empty?
A: Then you should return [“0->99”] as those ranges are missing.
Q: What if the given array contains all elements from the ranges? A: Return an empty list, which means no range is missing.


就是比较邻居的差值。
As it turns out, if we could add two “artificial” elements, –1 before the first element and 100 after the last element, we could avoid all the above pesky cases.

'''

class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, values, start, end ):
        results = [];  values = [start-1]+values+[end+1]   #补上两个多余的量。 来处理边界
        for i in range(1, len(values)):
            a = values[i];  b = values[i-1]
            if a-b>=2:  results.append(self.getRange(b+1, a-1))
        return results

    def getRange(self, l, r):
        return str(l) if l==r else str(l)+'->'+str(r)
s = Solution()
print s.findRange( [0, 1, 3, 50, 75], 0, 99)