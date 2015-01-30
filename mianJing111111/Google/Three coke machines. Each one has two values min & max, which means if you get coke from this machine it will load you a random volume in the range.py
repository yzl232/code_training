# encoding=utf-8
'''
Three coke machines. Each one has two values min & max, which means if you get coke from this machine it will load you a random volume in the range [min, max]. Given a cup size n and minimum soda volume m, show if it's possible to make it from these machines.
'''
# 和另一道coke的题目似乎不大一样。
#应当是用DFS
'''
Assume (x1,y1) , (x2,y2), (x3,y3) are the ranges of the three coke machines.
You have a range (m,n).

As stated before, m < X < Y < n for some (X,Y) to be obtained by a linear combination of the three machines.

Which means K1*x1 + K2*x2 + K3*x3 (= X) > m and K1*y1 + K2*y2 + K3 * y3 (=Y) < n

Take the second equation , we need to find all (K1,K2,K3) < n Start from n-1 (assume everything is an integer here. If not then we can scale the numbers till they become integers).
For every (k1,k2,k3) which satisfies the second equation see if it also satisfies the first equation. If yes , the problem can be solved . If no, decrement Sigma Ki*Xi to n-2 and repeat the algorithm.

It is a brute force approach almost. But it solves definitely.
'''



'''
比如三台machine(50, 100), (100, 200), (500, 1000).
n=110, m=40, yes.
n=90, m=40, no.
n=100, m=60, no
'''

#题目是possible。 我觉得如果是某种strategy保证一定实现的话。的话， 才是如下解法
#似乎是机器的范围一定要比杯子小？？？


class Solution:
    def getCoke(self, machines, n, m):
        self.machines = machines
        return self.dfs(n, m)

    def dfs(self, n, m):
        if n<0 or m<0: return False
        for row in self.machines:
            minV, maxV = row[0], row[1]
            if (minV>=m and maxV<=n) or self.dfs(m-minV, n-maxV): return True
        return False
s= Solution()
print s.getCoke([(50, 100), (100, 200), (500, 1000)],  110, 40)
print s.getCoke([(50, 100), (100, 200), (500, 1000)],  90, 40)
print s.getCoke([(50, 100), (100, 200), (500, 1000)],  100, 60)

#喝这道题目一样。


'''
A soda water machine,press button A can generate 300-310ml, button B can generate 400-420ml and button C can generate 500-515ml, then given a number range [min, max], tell if all the numers of water in the range can be generated.


class Solution:
    def generate(self, minV, maxV):
        dp = [False ] *(maxV+1);
        canGen=range(300, 311)+range(400, 421)+range(500, 515)
        for x in canGen: dp[x]=True
        for i in range(516, maxV+1):
            for j in canGen:
                if dp[i-j]:
                    dp[i] = True;  break
        return False not in dp[minV:maxV+1]
s = Solution()
print s.generate(700, 721)
'''