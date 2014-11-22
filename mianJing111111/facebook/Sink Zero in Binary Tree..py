# encoding=utf-8
'''
Sink Zero in Binary Tree. Swap zero value of a node with non-zero value of one of its descendants
so that no node with value zero could be parent of node with non-zero.


 o(n) solution

We should use a queue instead of a stack in order to swap always the top-most zero. Take this case for example:

        0
      /
    0
  /   \
2      0




一旦看到非0数，我们就看 queue

如果。 电面。 印象不深，可以直接念代码。  basically  dfs,   if root.val ==0:  queue.append.  else  we pop  and swap. and

'''
from collections import deque

class Solution:
    def sinkZero(self, root):
        self.q = deque([])
        self.dfs(root)

    def dfs(self, root):
        if not root: return
        if root.val ==0: self.q.append(root)   #queue里边存的是0
        elif len(self.q)>0:  #之前存在0元素
            tmp = self.q.popleft()
            root.val, tmp.val = tmp.val, root.val
            self.q.append(root)
        self.dfs(root.left)
        self.dfs(root.right)