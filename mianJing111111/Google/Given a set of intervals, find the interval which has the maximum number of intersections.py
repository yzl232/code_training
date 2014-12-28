# encoding=utf-8
'''
Given a set of intervals, find the interval which has the maximum number of intersections (not the length of a particular intersection).
'''
'''
A simple plane-sweep algorithm will do this in O(nlogn + m*n), where m is the maximum number of intersections with any single interval.

Sort the interval endpoints. Keep track of the active segments. When reaching a start point, increment the intersection counts of all active intervals, and set the new interval's intersection count to the number of active intervals (excluding itself). When reaching an end point, remove the interval from the active intervals.
'''


#O(nlogn ),.  m is the maximum going on meeting at the same time

'''
numIntersections[interval] = StartedEventsTill[end[interval]] - EndedEventsTill[start[interval]]-1
'''

#非常牛逼的解法。  排序用了O(nlogN)。 其他O(n)
class Solution:
    def findNumConference(self, intervals):
        affairs = [];   ret = 0; d={}
        for i in intervals:
            affairs.append((i[0], 1, i))
            affairs.append((i[1], -1, i))
            d[i] = 0
        affairs.sort()
        sCnt = 0;     eCnt=0
        for x in affairs:
            if x[1]==1:
                sCnt+=1
                d[x[-1]]=-eCnt
            elif x[1]==-1:
                eCnt+=1
                d[x[-1]]+=sCnt-1
        return d        #end

s = Solution()
print s.findNumConference([(5, 10), (6, 9), (11, 17), (15, 20), (16, 25), (10, 12)  ])