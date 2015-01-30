# encoding=utf-8
'''
1）what is BST?
(2) 可不可以里面有duplicate value.
(3) 如何handle duplicate value, 不同handle 策略有什么优缺点。
（4）然后选了一种我说的，把duplicate全放在left sub tree, 然后写一个function
判断是不是BST, 就是 validateBST
我写了一个最简单的，分析了复杂度， 是O(n^2), 问可不可以optimize,我说可以。
便写了一个O(n)的用low 和high 来bond.
'''
#不可以。
#这题面试的就是把BST的定义改成了left tree<=root, right tree < root然后让你写
# validateBST
#Many algorithms will specify that duplicates are excluded
#Most (that I've seen) specify left children as <= and right children as >.
# left <= root < right


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        self.ret = True
        self.dfs(root, -10**10, 10**10)
        return self.ret

    def dfs(self, root, l, h):      #BST一定要注意每次left, right同时要更新相应上下界为root.val。
        if not root: return
        if not (l<=root.val<h):  self.ret =False
        self.dfs(root.left, l, root.val)
        self.dfs(root.right, root.val, h)

'''
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.dfs(root, -10**10, 10**10)

    def dfs(self, root, l, h):      #BST一定要注意每次left, right同时要更新相应上下界为root.val。
        if not root: return True
        if not (l<=root.val<h): return False      #加了等号
        return self.dfs(root.left, l, root.val+1) and self.dfs(root.right, root.val, h) #改成了+1
'''