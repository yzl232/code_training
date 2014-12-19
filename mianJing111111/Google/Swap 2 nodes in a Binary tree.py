# encoding=utf-8
'''
意思是swap子树。
Swap 2 nodes in a Binary tree.(May or Maynot be a BST)
Swap the nodes NOT just their values.
(preferably in Java please..(My requirement not theirs :p))
ex:
5
/ \
3 7
/ \ /
2 4 6

swap 7 and 3

5
/ \
7 3
/ / \
6 2 4
'''
#注意跟面试官clear  一个是另一个parent的情况
#level order traversal
class Solution:
    def swap2(self, n1, n2, root):
        if n1==root or n2==root: return False
        if not n1 or not n2: return False
        pre, ret = [root], []   # 除了pre, cur之外，还用了第三个vals
        p1=p2=None;
        while pre and (not p1 or not p2):
            cur = []    #必须用array。 因为是有序的。 并且不会有重复
            for n in pre:
                if n1 in (n.left, n.right): p1 = n
                if n2 in (n.left, n.right): p2=n
                if n.left:    cur.append(n.left)
                if n.right:    cur.append(n.right)
            pre = cur
        if not p1 or not p2: return  False
        if p1.left ==n1: p1.left = n2
        else: p1.right = n2
        if p2.left == n2: p2.left =n1
        else: p2.right = n1