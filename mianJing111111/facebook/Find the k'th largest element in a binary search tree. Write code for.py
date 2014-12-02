# encoding=utf-8
'''
Find the k'th largest element in a binary search tree. Write code for

struct Node {
    int val;
    struct Node *left;
    struct Node *right;
} Node;

Node * kth_largest(Node *root, unsigned int k);



'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largest(self, root, k):
        self.k = k
        return self.dfs(root,  0)

    def dfs(self, root, count):
        if not root: return
        right = self.dfs(root.right,  count)
        if right: return right       #在右边。
        count+=1  #弄完一个右边子树。count +1。  看root是不是。    #每次在root 加1就好。 root代表一个节点。
        if count==self.k: return root
        return self.dfs(root.left,  count)
'''
跟findlevel有点像。 设置flag.  if left,  return left
'''


#这就是反向的traversal嘛。。。。right, root, left
# kth smallest number

class Solution2:
    def smallestK(self, root, k):
        self.k = k
        return self.dfs(root, 0)

    def dfs(self, root, count):
        if not root: return
        left = self.dfs(root.left, count)
        if left: return left
        count+=1
        if count==self.k:   return root
        return self.dfs(root.right, count)
