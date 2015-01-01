# encoding=utf-8
'''
写一个树（非二叉树）的iterator,注意不是traversal，并分析复杂度。
'''

class Iterator:
    # @param root, a tree node
    # @return a list of integers
    def __init__(self, root):
        self.stack = []
        self.pushL(root)

    def hasNext(self):
        if not self.stack: return False
        return True

    def next(self):
        if not self.hasNext():  return
        cur = self.stack.pop()
        self.pushL(cur)
        return cur.val

    def pushL(self, cur):
        self.stack+=cur.children[::-1]
#n-ary tree比普通的treee还要容易。