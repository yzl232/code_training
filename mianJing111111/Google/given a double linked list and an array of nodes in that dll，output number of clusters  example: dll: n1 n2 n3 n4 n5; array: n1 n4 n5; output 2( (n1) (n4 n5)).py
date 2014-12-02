# encoding=utf-8
'''
given a double linked list and an array of nodes in that dll，output number of clusters  example: dll: n1 n2 n3 n4 n5; array: n1 n4 n5; output 2( (n1) (n4 n5))
'''

class Solution:
    def getNumCluster(self, node, toFound):
        d = {i:1 for i in toFound}
        numNodes = len(toFound)
        prevInD = False
        result = 0
        while numNodes>0 and node:
            if node in d:
                numNodes-=1
                if not prevInD: result+=1
                prevInD = True
            else:  prevInD = False
            node = node.next
        return result
