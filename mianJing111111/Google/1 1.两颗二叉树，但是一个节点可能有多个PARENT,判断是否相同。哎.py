# encoding=utf-8
'''
1
1.两颗二叉树，但是一个节点可能有多个PARENT,判断是否相同。哎，STRUGGLE了很久
，最后写出来了，也不知道对不对。就是INORDER TRAVERSE的改一改
Example:
1
/ \
/ \
2 3
and
1
/ \
/ \
2 3
are identical. But
1
/ \
/ \
2   2
and
1
/ \
\ /
2
are NOT identical.
Also
1
/ \
/ \
2 \
/ \ /
/ \ /
2 2
\
\
2
and
1
/ \
/ \
2 \
/ \ \
/ \ \
2 2 /
\ /
\ /
2
are not identical.
'''

#看了几个例子。 sametree  能解决的

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):  #和symmitric tree题目一模一样
        if not p and not q: return  True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

