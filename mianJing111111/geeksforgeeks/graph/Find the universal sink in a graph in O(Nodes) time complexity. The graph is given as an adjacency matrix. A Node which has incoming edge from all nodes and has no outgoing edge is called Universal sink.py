# encoding=utf-8
'''
Find the universal sink in a graph in O(Nodes) time complexity. The graph is given as an adjacency matrix.
A Node which has incoming edge from all nodes and has no outgoing edge is called Universal sink


就是celebrity  problem
'''


'''
O(n)

If A knows B, then A can’t be celebrity. Discard A, and B may be celebrity.
If A doesn’t know B, then B can’t be celebrity. Discard B, and A may be celebrity.
就这2句话。非常巧妙
'''

class Solution:
    def findCelebrity(self, nodes):
        stack = nodes[:]
        while len(stack)>1:  #eliminating stage
            u = stack.pop()
            v = stack.pop()
            if self.hasLinkTo(u, v):
                stack.append(v)
            else:   stack.append(u)
        if not self.verify(nodes, stack[0]): return False   # no celebrity.
        return stack[0]

    def verify(self, peoples, c):
        for p in peoples:
            if not self.hasLinkTo(p, c): return False
        return True

    def hasLinkTo(self, p1, p2):
        pass