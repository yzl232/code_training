# encoding=utf-8
'''

Given n intervals [si, fi], find the maximum number of overlapping intervals

实际上就是会议室问题。

和leetcode的 insert interval类似。

Given an array of meetings, find out the minimum number of conference rooms required.

class Meeting
{
long startTime;
long endTime;
};




sort  all si and ei gloablly,
set needed = 0,
scan all sorted si and ei , see si, ++needed, see ei, --needed
take the max number you get for needed during the scanning.


另外也是facebook的题目。
input:
04: (......................)
07:              (.........)
09: (........).
11:     (..).
12:        (............)
15:                  (..)

struct Employee {
i64 id,
i64 startTime,
i64 endTime
};

output:
2004-2007: 2 // 4,9
2007-2008: 3 // 4,9,11.
2008-2009: 3 // 4,9,12
2009-2011: 2
2011-2013: 3
2013-2014: 4
2014-2015: 2

。。。我几个月前面G家intern转正也问的这道题。。。当时也没想好怎么做。。。也栽了T T
这道题可以从左往右扫描时间线。全局维护一个count，如果扫到的时间是start time，就输出当前count以后++count。如果扫到的是end time，就输出count以后--count。
排序时间线用O(nlgn)，扫一遍O(n)。


这题和“一堆会议的start和end，问最少需要多少会议室”，一样。所有时间排序到一
: 起，线性走一遍，遇到start +1，end -1. 走的过程中得最大值就是解。
: 4]
'''

class Solution:
    def findNumConference(self, intervals):
        affairs = [];  count = 0; result = 0
        for i in intervals:
            affairs.append((i[0], 1))
            affairs.append((i[1], -1))
        affairs.sort()
        for i in affairs:
            count+=i[-1]
            result = max(result, count)
        return result
s = Solution()
print s.findNumConference([(5, 10), (6, 9), (11, 17), (15, 20), (16, 25), (10, 12)  ])


'''

感觉跟leetcode上面的interval那题很相似，简单一点点。
// Given a array of pairs where each pair contains the start and end time of
a meeting (as in int),
// Determine if a single person can attend all the meetings
// Input array(pair(1,4), pair(4, 5), pair(3,4), pair(2,3))
// Output: False
'''


'''
// Given a array of pairs where each pair contains the start and end time of
a meeting (as in int),
// Determine if a single person can attend all the meetings
// Input array(pair(1,4), pair(4, 5), pair(3,4), pair(2,3))
// Output: False

因为（2，3）  完全包含在（1，4）.  所以为False

第二题就按pair.first sort一下 然后从头扫到尾 如果 arr[i+1][2]<arr[i+1][2]

'''





'''
刚听别人说的，转过来，代码好细致：

Given a collection of user login logs, print all intervals at which there is a change in the total # of users online.

Class Log:

int login_time
int logout_time


user 1:
login_time: 0
logout_time: 1

user 2:
login_time: 1
logout_time: 3

user 3:
login_time: 0
logout_time: 2


Output:
so print

0-2  2 users online
2-3 1 user online
3 - infinity 0 user online




'''

class Solution2: #比较难写
    def findNumConference(self, intervals):
        affairs = []
        for i in intervals:
            affairs.append((i[0], 1))
            affairs.append((i[1], -1))
        affairs.sort()
        prev =i =count= 0
        while i<len(affairs) and affairs[i][0]==0:       #因为0增加，不用打印。 所以无所谓
            count+=affairs[i][-1]     #猛加
            i+=1
        while i<len(affairs):
            old = count
            now =i
            while i<len(affairs) and affairs[i][0]==affairs[now][0]: #碰到同一时间的特殊情况
                count+= affairs[i][-1]
                i+=1
            if count!=old:
                print prev, '~',affairs[now][0], 'have:',  old, "user online"
                prev = affairs[now][0]  #不等的时候，更新
        print prev, '~ infinity', 'have:',0, "user online"
s = Solution2()
s.findNumConference([(0,1), (1,3), (0,2)  ])