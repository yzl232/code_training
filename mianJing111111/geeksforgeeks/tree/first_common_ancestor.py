__author__ = 'zhenglinyu'
class Solution:
    def find_Ancestor(self, p, q):
        hashtable = {}
        while p or q:
            if p:
                if p in hashtable: return p
                hashtable[p] = 1
                p = p.parent
            if q:
                if q in hashtable: return q
                hashtable[q] = 1
                q = q.parent
        return

#O(n) and O(n)




class Solution2:
    def find_Ancestor2(self, p, q):
        h1 = self.getHeight(p)
        h2 = self.getHeight(q)

        if h1> h2:
            h1, h2 = h2, h1
            p, q = q, p

        # h2 is bigger
        dh = h2 - h1
        for i in range(dh):
            q = q.parent
        while p and q:
            if p == q: return p
            p = p.parent
            q = q.parent
        pass


    def getHeight(self, p):
        height = 0
        while p:
            height+=1
            p = p.parent
        return height
# O(1) and O(n)


class SolutionRecursin:
    def findAncestor(self, root, p, q):
        if not root: return
        if root == p or root == q: return root
        l = self.findAncestor(root.left, p, q)
        r = self.findAncestor(root.right, p, q)
        if l and r: return root  #2个都找到。在root
        if l: return l  #找到一个。在左边
        else: return r  #找到一个。在右边


'''
The idea is to traverse the tree starting from root. If any of the given keys (n1 and n2) matches with root, then root is LCA (assuming that both keys are present). If root doesn’t match with any of the keys, we recur for left and right subtree. The node which has one key present in its left subtree and the other key present in right subtree is the LCA. If both keys lie in left subtree, then left subtree has LCA also, otherwise LCA lies in right subtree.
'''