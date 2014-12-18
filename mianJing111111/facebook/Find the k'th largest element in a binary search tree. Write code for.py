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
        return self.dfs(root,  k)

    def dfs(self, root, cnt):
        if not root: return
        r = self.dfs(root.right,  cnt)
        if r: return r       #在右边。
        cnt-=1  #弄完一个右边子树。count -1  看root是不是。  #每次在root 加-就好。 root代表一个节点。
        if cnt==0: return root
        return self.dfs(root.left,  cnt)
'''
跟findlevel有点像。 设置flag.  if left,  return left
'''


#这就是反向的traversal嘛。。。。right, root, left
# kth smallest number

class Solution2:
    def smallestK(self, root, k):
        return self.dfs(root, k)

    def dfs(self, root, cnt):  #  (O(n))
        if not root: return
        l = self.dfs(root.left, cnt)
        if l: return l  #这里可以优化很多了
        cnt-=1
        if cnt==0:   return root
        return self.dfs(root.right, cnt)


#如果用augmented data structure.  O(logN)

#想法比较赞。 应该不用写代码

'''
面经  finding k-th largest element in O(N) without modifying the node, and then same k-th largest element in log(N) time keeping the size of the subtree in each node.
'''




#find the kth smallest element
'''
et each node in the BST have a field that returns the number of elements in its left and right subtree. Let the left subtree of node T contain only elements smaller than T and the right subtree only elements larger than or equal to T.

Now, suppose we are at node T:

    k == num_elements(left subtree of T), then the answer we're looking for is the value in node T
    k > num_elements(left subtree of T) then obviously we can ignore the left subtree, because those elements will also be smaller than the kth smallest. So, we reduce the problem to finding the k - num_elements(left subtree of T) smallest element of the right subtree.
    k < num_elements(left subtree of T), then the kth smallest is somewhere in the left subtree, so we reduce the problem to finding the kth smallest element in the left subtree.

This is O(log N) on average (assuming a balanced tree).
'''
class Solution:
    def find(self, root, k): #BST.是平衡的。
        if not root or root.size<k: return
        if root.left:
            n = root.left.size
            if n ==k-1: return root
            elif n <k-1: return self.find(root.right, k-1-n)
            else: return self.find(root.left, k)
        else:
            return self.find(root.right, k-1)
