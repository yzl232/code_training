# encoding=utf-8
'''
Find the distance between two keys in a binary tree, no parent pointers are given. Distance between two nodes is the minimum number of edges to be traversed to reach one node from other.


 Time complexity of the above solution is O(n) as the method does a single tree traversal.

 Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)

'lca' is lowest common ancestor of n1 and n2
Dist(n1, n2) is the distance between n1 and n2.




geeks的答案过于复杂了。 害死我了。
只要找到n1与lca的距离，  n2与lca的距离，  然后相加就可以了。  真二。


1)first find LCA of n1 and n2.

2)a=find distance of n1 from lca.

3)b=find distance of n2 from lca.

4) return a+b;

'''
class Solution:
    def findAncestor(self, root, p, q):
        if not root: return
        if root == p or root == q: return root
        l = self.findAncestor(root.left, p, q)
        r = self.findAncestor(root.right, p, q)
        if l and r: return root  #2个都找到。在root
        if l: return l  #找到一个。在左边
        else: return r  #找到一个。在右边

    def findShortestPath(self, root, a, b):
        self.path = []
        lca = self.findAncestor(root, a,b)
        self.a = a; self.b = b
        self.shortestPath(lca, [])
        path1 = self.path[0][::-1] #逆转一下path
        path2 = self.path[1][1:]   #多了一个root
        return path1+path2

    def shortestPath(self, root, tmpPath):    #然后就是普通的DFS从ancester找path
        if not root: return
        if root.val == self.a.val or root.val == self.b.val:
            self.path.append(tmpPath+[root.val])
            return
        self.shortestPath(root.left,tmpPath+[root.val])
        self.shortestPath(root.right,tmpPath+[root.val])

#如果只是求距离

class Solution5:
    def findAncestor(self, root, p, q):
        if not root: return
        if root == p or root == q: return root
        l = self.findAncestor(root.left, p, q)
        r = self.findAncestor(root.right, p, q)
        if l and r: return root  #2个都找到。在root
        if l: return l  #找到一个。在左边
        else: return r  #找到一个。在右边

    def findLevel(self, root, node, level): #找一个子节点到root得距离
        if not root: return -1  #没找到，就是-1
        if root == node: return level
        d = self.findLevel(root.left, level+1)
        if d !=-1: return d
        return self.findLevel(root.right,  level+1)

    def findDistance(self, root, n1, n2):
        lca = self.findAncestor(root, n1, n2)
        d1 = self.findLevel(lca, n1, 0)
        d2 = self.findLevel(lca, n2, 0)
        return d1+d2