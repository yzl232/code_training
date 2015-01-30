# encoding=utf-8
'''
这道题目败了很多次，强烈地显示了tree方面的不足

另外变化非常多。 以下5个代码都需要掌握

parent pointer的情况
'''
class Solution:
    def find_Ancestor(self, p, q):
        d = set()     #set就是hashtable。
        while p or q:
            if p:
                if p in d: return p
                d.add(p)
                p = p.parent
            if q:
                if q in d: return q
                d.add(q)
                q = q.parent
        return
#O(n) and O(h)


# 和那道linkedlist的类似。
class Solution2:
    def find_Ancestor2(self, p, q):
        h1 = self.getH(p); h2=self.getH(q)
        diff = abs(h1-h2)
        if h1<h2:  p, q = q, p
        for i in range(diff): p=p.parent
        while p and q:
            if p==q: return p
            p = p.parent;  q=q.parent

    def getH(self, p):
        h = 0   #找特殊情况。比如p==root,  很容易写
        while p:
            h+=1
            p = p.parent
        return h
# O(1) and O(h)
#直接写最优解就好了。  第一种解法提一下就好。

'''
以下是无parent pointer的情况
'''

'''
Lowest Common Ancestor in a Binary Search Tree.
这个是bst的情况  。 时间复杂度只要  O(logN)。 用到stack recursion space

只要是与bst相关的题目，就少不了比较val大小， start, end等等
'''




'''
class Solution8:
    def findlca(self, root, v1, v2):
        if not root: return
        if root.val > v1 and root.val > v2:  return self.findlca(root.left, v1, v2)#都在右边
        if root.val < v1 and root.val <v2:   return self.findlca(root.right, v1, v2)#都在左边
        return root
'''


#如果用iterative可以做到O(1) space  O(logN) time
#很巧妙
# BST  O(logN)的题目一般都是可以while来做
class Solution9:
    def findLCA(self, root, v1, v2):
        while root:
            if root.val>max(v1, v2): root=root.left      #偏大就往右。 偏小就往左
            elif root.val <min(v1, v2): root=root.right
            else: return root


'''
Lowest Common Ancestor in a Binary Tree  普通情况
O(n)
Given a binary tree (not a binary search tree) and two values say n1 and n2, write a program to find the least common ancestor.
'''
#存path的方法。 大概看一下geeksforgeeks的原理， 提一下就好， 因为不是最优解。

#最优解
class SolutionRecursin:
    def anc(self, root, p, q):        #和findlevel  search的题目是有点像的, 往下seach x ，  往下search p, q
        if not root: return  #没找到
        if root in (p, q): return root  #没找到
        l = self.anc(root.left, p, q)
        r = self.anc(root.right, p, q)
        if l and r: return root  #2个都找到。在root   # 这一行只会运行一次。
        if l: return l  #找到一个。都在左边      .
        else: return r  #找到一个。都在右边