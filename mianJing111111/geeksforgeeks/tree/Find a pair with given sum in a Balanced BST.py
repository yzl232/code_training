# encoding=utf-8
'''
Find a pair with given sum in a Balanced BST

Given a Balanced Binary Search Tree and a target sum, write a function that returns true if there is a pair with sum equals to target sum, otherwise return false. Expected time complexity is O(n) and only O(Logn) extra space can be used. 。


'''
# 因为是balanced BST.所以可以达到LogN space.
# flatten

class Solution:
    # @param root, a tree node  #注意这道题目不是binary search tree  。
    # @return nothing, do it in place  #他的顺序是   in order  left, root, right
    def flatten(self, root):  #我们反过来，就是right, root, left
        self.head = None
        self.dfs(root)
        return self.head

    def dfs(self, root):
        if not root: return
        self.dfs(root.right)              #也是三步
        if self.head:  self.head.left = root  #在这里，还可以设置tail节点。 如果有必要
        root.right = self.head  #右边连上
        self.head = root    #更新head
        self.dfs(root.left)

class Solution3:
    def twoSum(self, head, tail, target):
        while head.val < tail.val:
            cur = head.val + tail.val
            if cur == target: return True
            elif cur<target:  head=head.next
            else: tail = tail.prev

#  第二种不能改结构

'''
Given a BST and a value x. Find two nodes in the tree whose sum is equal x. Additional space: O(height of the tree). It is not allowed to modify the tree
'''
# http://www.geeksforgeeks.org/find-a-pair-with-given-sum-in-bst/
#原理： in order traversal 用stack的做法。 stack只存logN数目的node。 所以空间是logN
#用2个stack
class Solution5:
    def find(self, root, target):
        s1 = []; s2=[]
        done1=done2=False
        cur1 = root;  cur2= root.right
        val1=val2=None
        while True:
            while done1:
                while cur1:
                    s1.append(cur1)
                    cur1 = cur1.left
                if not s1:  done1=True
                cur1 = s1.pop()
                val1 = cur1.val
                cur1 = cur1.right
                done1 =True
            while done2:
                while cur2:
                    s2.append(cur2)
                    cur2 = cur2.right
                if not s2:  done2 = True
                cur2 = s2.pop()
                val2 = cur2.val
                cur2 = cur2.left
                done2=True
            if val1+val2==target:  return val1, val2
            elif val1+val2<target:   done1=False
            else: done2=False
            if val1>=val2: return False