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
        self.rets = []
        lca = self.findAncestor(root, a,b)
        self.a = a; self.b = b
        self.shortestPath(lca, [])
        path1 = self.rets[0][::-1] #逆转一下path
        path2 = self.rets[1][1:]   #多了一个root
        return path1+path2

    def shortestPath(self, root, cur):    #然后就是普通的DFS从ancester找path
        if not root: return
        if root in (self.a, self.b):
            self.rets.append(cur+[root.val])
            return
        self.shortestPath(root.left,cur+[root.val])    #path这种都是晚一步。  因为不知道left是不是有val值
        self.shortestPath(root.right,cur+[root.val])

#如果只是求距离

class Solution5:
    def findAncestor(self, root, p, q):
        if not root: return
        if root == p or root == q: return root
        l = self.findAncestor(root.left, p, q)
        r = self.findAncestor(root.right, p, q)
        if l and r: return root      #2个都找到。在root
        if l: return l        #找到一个。在左边
        else: return r      #找到一个。在右边

    def findLevel(self, root, node):
        self.ret = None; self.node = node
        self.dfs(root, 1)
        return self.ret

    def dfs(self, root, level): #找一个子节点到root得距离
        if not root: return
        if self.ret: return
        if root == self.node:     self.ret = level
        self.dfs(root.left, level+1)
        self.dfs(root.right,  level+1)

    def findDistance(self, root, n1, n2):
        lca = self.findAncestor(root, n1, n2)
        d1 = self.findLevel(lca, n1)
        d2 = self.findLevel(lca, n2)
        return d1+d2