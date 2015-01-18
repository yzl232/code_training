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


'''
 Nth largest from tree. Given a binary search tree where the left node is
smaller and the right node is larger. Calculate the Nth largest number in
the tree throwing exception when there is less than N elements in the tree.
'''


#本题是google的高频题目

# 用inorder  travsersal 比较简单。

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root, n):
        self.cnt=n;  self.ret = None
        self.dfs(root)
        return self.ret

    def dfs(self, root):
        if not root or self.ret:       return  #已经找到了。 不用管了。
        self.dfs(root.right)
        self.cnt-=1
        if self.cnt==0:   self.ret = root.val
        self.dfs(root.left)


'''
#下面这个太复杂了。
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


'''
跟findlevel有点像。 设置flag.  if left,  return left
'''


#这就是反向的traversal嘛。。。。right, root, left
# kth smallest number



# in order traversal

#这个方法也很好
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root, k):
        stack = [];  cur = root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            if not stack: break
            cur = stack.pop()
            k-=1
            if k==0:  return cur
            cur = cur.right
        return


#递归法。
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
class Solution7:
    def find(self, root, k): #BST.是平衡的。
        if not root or root.size<k: return
        n = root.left.size if root.left else 0
        if n ==k-1: return root
        elif n <k-1: return self.find(root.right, k-1-n)
        else: return self.find(root.left, k)



#下面是建立size的方法
    def dfs(self, root):  #更新size。  复制自更新sum  value那道。
        if not root: return 0
        root.size = 1
        if root.left: root.size+=self.dfs(root.left)
        if root.right: root.size +=self.dfs(root.right)
        return root.size

'''
# G家题目

刚开始我用global variable做的
后来小哥说不用额外空间，然后这里卡住了。。最后他提示让用不断求子树size的方法做，然后写求子树size的地方也卡了一段时
'''



'''
#又是G家题目。
You have a binary tree where each node knows the number of nodes in its sub-tree (including itself).

Given a node n and an int k,
write a function to return the kth
node in an in order traversal.
Can you do this non recursively
'''

def find(root, k): #和递归一样的
    if not root or root.size<k: return
    while root:
        n = root.left.size if root.left else 0
        if n ==k-1: return root
        elif n <k-1:
            root = root.right
            k=k-1-n
        else:
            root=root.left