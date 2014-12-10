# encoding=utf-8
'''

Find if there is a triplet in a Balanced BST that adds to zero

Given a Balanced Binary Search Tree (BST), write a function isTripletPresent() that returns true if there is a triplet in given BST with sum equals to 0, otherwise returns false. Expected time complexity is O(n^2) and only O(Logn) extra space can be used. You can modify given Binary Search Tree. Note that height of a Balanced BST is always O(Logn)
For example, isTripletPresent() should return true for following BST because there is a triplet with sum 0, the triplet is {-13, 6, 7}.


最naive的方法是in order 转化成array,   3-sum


'''

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

class Solution5:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, head, tail):
        i = head; tail = head
        while tail.next: tail=tail.next
        while i and i.next and i.next.next:
            l = i.next;  r = tail; target = 0-i.val
            while l.val < r.val:
                if l.val+r.val == target: return True
                elif l.val+r.val < target:   l = l.next
                else: r = r.pre
            i = i.next
        return False