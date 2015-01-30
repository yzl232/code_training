# encoding=utf-8
'''
There are at most eight servers in a data center. Each server has got a capacity/memory limit. There can be at most 8 tasks that need to be scheduled on those servers. Each task requires certain capacity/memory to run, and each server can handle multiple tasks as long as the capacity limit is not hit. Write a program to see if all of the given tasks can be scheduled or not on the servers?

Ex:
Servers capacity limits: 8, 16, 8, 32
Tasks capacity needs: 18, 4, 8, 4, 6, 6, 8, 8
For this example, the program should say 'true'.

Ex2:
Server capacity limits: 1, 3
Task capacity needs: 4
For this example, program should return false.

Got some idea that this needs to be solved using dynamic programming concept, but could not figure out exact solution.
'''

#和leetcode  sudoku特别像
class Solution:
    def canArrange(self, servers, tasks):
        ok = [False]*len(tasks)
        return self.dfs(servers, tasks, ok)

    def dfs(self, servers, tasks, ok):
        if False not in ok: return True
        for i in range(len(tasks)):  #尝试每个servers都试试每个tasks
            if not ok[i]:
                ok[i] = True
                for j in range(len(servers)):
                    if servers[j]>=tasks[i]:
                        servers[j]-=tasks[i]
                        if self.dfs(servers, tasks, ok): return True
                        servers[j]+=tasks[i]
                ok[i] = False
        return False

s = Solution()
print s.canArrange([8, 16, 8, 32],[18, 4, 8, 4, 6, 6, 8, 8] )