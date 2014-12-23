# encoding=utf-8
'''
Given a timer time() with nanosecond accuracy and given the interface

interface RealTimeCounter:
    void increment()
    int getCountInLastSecond()
    int getCountInLastMinute()
    int getCountInLastHour()
    int getCountInLastDay()

implement the interface. The getCountInLastX functions should return the number of times increment was called in the last X.

'''
import collections

#http://stackoverflow.com/questions/17562089/how-to-count-number-of-requests-in-last-second-minute-and-hour

class Solution():
    def __init__(self):
        self.secQ = collections.deque(maxlen = 1)
        self.minQ = collections.deque(maxlen = 60)
        self.HourQ = collections.deque(maxlen = 60)
        self.dayQ = collections.deque(maxlen = 24)
        self.secCnt = 0
    def foo(self):
        self.secCnt+=1

    def addToSecqueue(self):
        self.minQ.append(self.curCount)
        self.secQ.append(self.secQ)
        self.secCnt=0

#每秒钟把当前的count加进去。
#每分钟把minQ的和求出来， 加入到HourQ
#每小时把HourQ的和求出来，加入到dayQ
# 基本原理是类似的
# circular queue