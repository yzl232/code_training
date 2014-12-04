# encoding=utf-8
'''
In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find the stranger (celebrity) in minimum number of questions.

We can describe the problem input as an array of numbers/characters representing persons in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns true if A knows B, false otherwise. How can we solve the problem, try yourself first.

We measure the complexity in terms of calls made to HaveAcquaintance().


'''


'''
O(n)

If A knows B, then A can’t be celebrity. Discard A, and B may be celebrity.
If A doesn’t know B, then B can’t be celebrity. Discard B, and A may be celebrity.
就这2句话。非常巧妙
'''

class Solution:
    def findCelebrity(self, peoples):
        stack = peoples[:]
        while len(stack)>1:  #eliminating stage
            u = stack.pop()
            v = stack.pop()
            if self.haveAcquaintance(u, v):
                stack.append(v)
            else:   stack.append(u)
        if not self.verify(peoples, stack[0]): return False   # no celebrity.
        return stack[0]

    def verify(self, peoples, c):
        for p in peoples:
            if not self.haveAcquaintance(p, c): return False
        return True

    def haveAcquaintance(self, p1, p2):
        pass


'''
后面的暴力法。懒得看了


Graph:

We can model the solution using graphs. Initialize indegree and outdegree of every vertex as 0. If A knows B, draw a directed edge from A to B, increase indegree of B and outdegree of A by 1. Construct all possible edges of the graph for every possible pair [i, j]. We have NC2 pairs. If celebrity is present in the party, we will have one sink node in the graph with outdegree of zero, and indegree of N-1. We can find the sink node in (N) time, but the overall complexity is O(N2) as we need to construct the graph first.

建立一个双向图。
找indegree = n-1,   outdegree = 0
暴力法。  O(n2)
比较n(n-1)次就可以建立图
'''

#暴力法
class Node:
    def __init__(self, p):
        self.id = p.id
        self.inDegree = 0
        self.outDegree = 0


class BruteForce:
    def findCelebrity(self, peoples ):
        peoplesNodes = []
        for p in peoples:
            peoplesNodes.append(Node(p))
        for i in range(len(peoplesNodes)):
            for j in range(i+1, len(peoplesNodes)):
                if self.haveAcquaintance(peoples[i], peoples[j]):
                    peoplesNodes[i].outDegree+=1
                    peoplesNodes[j].inDegree +=1
        for i in range(len(peoplesNodes)):
            n = peoplesNodes[i]
            if n.inDegree == len(peoples)-1 and n.outDegree == 0:
                return


    def haveAcquaintance(self, p1, p2):
        pass
