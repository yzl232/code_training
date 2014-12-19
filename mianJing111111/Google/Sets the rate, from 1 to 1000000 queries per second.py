# encoding=utf-8
'''
This is two questions I got from a google interview. Not very sure how to solve it. Any comments would be appreciated.

1.
interface RateLimit {
/** Sets the rate, from 1 to 1000000 queries per second */
void setQPS(int qps);

/** accept or reject a request, called when request is received */
boolean allowThisRequest();
}

brief example:
server instantiates your object, calls setQPS(1)
at at time t, user1 makes a request, allowThisRequest() returns true
at time t+0.01 sec, user2 makes a request, allowThisRequest() returns false
at at time t+1, user4 makes a request, allowThisRequest() returns true
at time t+5 sec, user3 makes a request, allowThisRequest() returns true
'''
import  time
#就是每秒钟允许调用多少次的变体
#设计一个function: bool cancall(), 保证每秒钟内return true的数量小于 N,

#做法。starttime,  <1的时候只更新cnt， >1的时候重置cnt, startTIme
class Solution3:
    def __init__(self, N):
        self.startTime = -1
        self.count = 0
        self.N = N

    def setQPS(self, N):
        self.N = N

    def allowThisRequest(self):
        curr_time = int(time.time())
        if curr_time - self.startTime < 1 and self.count<self.N:
            self.count+=1  #不更新startTime
            return True
        elif curr_time-self.startTime>=1:
            self.count=1
            self.startTime = curr_time    #到这里更新startTime
            return True
        else:  #过多了。 啥也不做
            return False