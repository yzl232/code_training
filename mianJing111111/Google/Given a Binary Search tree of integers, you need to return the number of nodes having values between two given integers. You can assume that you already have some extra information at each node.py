# encoding=utf-8
'''
Given a Binary Search tree of integers, you need to return the number of nodes having values between two given integers. You can assume that you already have some extra information at each node (number of children in left and right subtrees !!).
'''

'''
Interesting, this was one of the questions of my second interview. This was my answer:
- Suppose we know the size of the left subtree for each node.
- We want the number of values in the interval [A, B]. This is the same as the number of values up to B minus the number of values less than A.
- So we can reduce this question to finding the number of values up to X.
1) Start at the root
2a) If the value we search is less or equal to current node value. Then this node and all values to the right are larger or equal to this value and we can ignore them. Recurse on the left subtree
2b) The value we search is larger than the current node value. Then this node and all values in the left subtree are less than this value. Recurse on the right subtree.

On a balanced BST, this algorithm takes O(log N) time...
'''
class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 1

class Solution:
    def getLess(self, root, v):
        ret =0
        while root:
            if root.val>=v: root=root.left
            else:
                ret+=1+root.left.size
                root=root.right
        return ret

    def solve(self, root, start,end):
        return self.getLess(root, end+1)-self.getLess(root, start)   # start, end.  inclusive。  所以是end+1


'''
class Solution:
    def getLess(self, root, v):
        if not root: return 0
        if v<=root.val: return self.getLess(root.left, v)
        return 1+root.leftN + self.getLess(root.right, v)

    def solve(self, root, start,end):
        return self.getLess(root, end+1)-self.solve(root, start)
'''

#比较巧妙。比较难。
#因为是augmented data structure