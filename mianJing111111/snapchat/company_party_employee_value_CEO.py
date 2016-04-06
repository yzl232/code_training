# encoding=utf-8

'''


You are given an organization hierarchy tree (n-ary tree). Every employee (node) has some value (can be -ve or +ve). You have to host a party and have to invite employees such that the total value (summation of each node value) of all the employees is maximum.

there is a rule: no one likes to see their bosses in the party. So you cant invite an employee's immediate boss or subordinate.

You can skip more than 1 level if it gives you maximum value.


uppose we are planning a company party.  The company organizational
structure is so that there is a single Owner who runs the place.
Everyone has one direct manager, but a manager may have any number of direct.鏈枃鍘熷垱鑷�1point3acres璁哄潧
reports.  Everyone must report to the owner, possibly indirectly.
Each employee has associated with him a non-negative “fun” value.  What we
want to do is invite the set of employees to make the party as fun as
possible.

Here is the only constraint:  If you invite an employee, you cannot invite
that employee’s direct manager.
   A
B     C
I J     D  E
   F G H

If we include A:  total fun value should Fun(A)=sum_{i=I,J,D,E}(Fun(i))
no A:      Fun(A)={Fun(B)+Fun(C)}. Waral 鍗氬鏈夋洿澶氭枃绔 ,
It’s legal to invite B and C
Or it’s legal to invite D, E, A, but you cannot invite D and C, or B and A.

后来复习时才注意到这是party at Hali-Bula,经典树形dp。面试时现推的树形dp，才
拿到positive feedback。




 Professor Stewart is consulting for the president of a corporation that is planning a company party. The company has a hierarchical structure; that is, the supervisor relation forms a tree rooted at the president. The personnel office has ranked each employee with a conviviality rating, which is a real number. In order to make the party fum for all attendees, the president does not want both an employee and his or her immediate supervisor to attend.

     Professor Stewart is given the tree that describes the structure of the corporation, using theleft-child, right-sibling representation. Each node of the tree holds, in addition to the pointers, the name of an employee and that employee’s conviviality ranking. Describe an algorithm to make up a guest list that maximizes the sum of the conviviality ratings of the guests. Analyze the running time of your algorithm.

   Stewart教授是一家公司总裁的顾问，这家公司计划一个公司聚会。这个公司有一个层次式的结构；也就是说，管理关系形成一棵以总裁为根的树。人事部给每个雇员以喜欢聚会的程度来排名，这是个实数。为了使每个参加者都喜欢这个聚会，总裁不希望一个雇员和他（她）的直接上司同时参加。

   Stewart教授面对一棵描述公司结构的树，使用了左子女、右兄弟表示法。树中每个结点除了包含指针，还包含雇员的名字和该雇员喜欢聚会的排名。描述一个算法，它生成一张客人列表，使得客人喜欢聚会的程度的总和最大。分析你的算法的执行时间。

'''
#好像就是 House Robber III, 但是不是只有左右子树。 有多个树。



class Solution(object):
    def rob(self, root):
        def dfs(x):
            if not x: return (0, 0)
            s0 = 0;  s1=0
            for y in x.children:
                t0, t1 = dfs(y)
                s0+=t0
                s1+=t1
            return (s1, max(s1, s0 + x.val))
        return dfs(root)[1]

class TreeNode:
    def __init__(self, x, children = []):
        self.children = children
        self.val = x
a = TreeNode(5)
b = TreeNode(7)
c = TreeNode(8)
e = TreeNode(9)
c.children = [e]
a.children = [b, c]
s = Solution()
print s.rob(a)

'''
noRoot(node) = curMax(node.left) + curMax(node.right)

curMax(node) = max( noRoot(node.left)+noRoot(node.right)+node.value, noRoot(node) ).



假设如下：

dp[i][0]表示不选i结点时，i子树的最大价值

dp[i][1]表示选i结点时，i子树的最大价值

列出状态方程

dp[i][0] = sum(max(dp[u][0], dp[u][1]))

(如果不选i结点，u为结点i的儿子)

dp[i][1] = sum(dp[u][0]) + val[i]

(如果选i结点，val[i]表示i结点的价值)

最后就是求max(dp[root][0], dp[root][1])

'''
#有点像这道题。 geeks: Given a Binary Tree, find size of the Largest Independent Set(LIS)