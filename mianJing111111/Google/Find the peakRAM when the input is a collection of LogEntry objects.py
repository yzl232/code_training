# encoding=utf-8
'''
public class LogEntry {
 public final long startTime; // start time of a job in millisec granularity
 public final long endTime; // end time of a job in millisec granularity.
 public final long ram; // the amount of ram the job occupies.
 public final long jobId;
 ... constructor ...
}

running total of RAM
|
|             3GB
|           -----
|      2GB
|     ------
| 1GB                       -----------
|-----           -----------
|
|____________________________________________________time

Find the peakRAM when the input is a collection of LogEntry objects
'''


'''
Use a treemap to keep a chronologically sorted set of events that map to the amount of RAM created or destroyed. Iterate over the keys to keep a running total of RAM used while keeping track of the highest amount.
'''

#就是会议室安排问题

class Solution:
    def findNumConference(self, intervals):
        affairs = [];  cnt = 0; ret = 0
        for i in intervals:
            affairs.append((i[0], i[2]))
            affairs.append((i[1], -i[2]))
        affairs.sort()
        for i in affairs:
            cnt+=i[-1]
            ret = max(ret, cnt)
        return ret
s = Solution()
print s.findNumConference([(5, 10, 5), (6, 9, 7), (11, 17, 10), (15, 20, 21), (16, 25, 3), (10, 12,15)  ])