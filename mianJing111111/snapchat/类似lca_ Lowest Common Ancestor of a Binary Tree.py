'''
 Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

第一轮，面经题，给你一个employer类，里面有雇员name，直属boss两个成员，要你写一个函数，给ceo的object和employer1 和employer2的名字，注意这里是string不是object，要你返回这两个人最近的boss。刚开始以为是lca问题，所以立马秒了。但是面 试官居然说和经典lca不一样！这里假如e1是e2的直属上司，那么返回的是e1的直属上司而不是e1. 我平时用的算法针对这个还确实不太好改，改来改去都有点问题，加上传入的是string而不是employer对象，搞了很久最后也没弄出来。。。 平时刷题什么的还是要多看几种方法并且记住普遍性强的算法比较好一些。


看到第一题深有感触。。一次电面也是遇到了LCA的题，按照Leetcode的recursion方法就给秒了， 结果面试官说公共祖先不能包含任何一个node（当时我听到的时候也是shock了一下）。。。最后也是改来改去都没改好recursion的方法。 后来想了一下感觉可以这样做，还是先求LCA，如果是LCA就是p,q中的任意一个node(说明p是q的祖先或者q是p的祖先)，那么再求一下LCA的 parent。。
'''

class Solution(object):
    def lca(self, root, p, q, parent):
        if not root: return 
        if root in (p, q): return parent
        l, r = self.lca(root.left, p, q, root), self.lca(root.right, p, q, root)
        return root if (l and r) else (l or r)
        
    def getBoss(self, root, p, q):
        return self.lca(root, p, q, None)