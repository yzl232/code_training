# encoding=utf-8
'''
给你getParent(), getNextSibling(), getFirstChild()

要实现getNextNode(node)

比如，
1
1.1
1.2
1.2.1
1.2.2
1.3
2
2.1
2.2
2.2.1
3
'''

'''
有子节点,返回子节点.
没子节点,看兄弟节点.
没兄弟开始回溯父节点找父节点兄弟,找到或者到根退出?
唯一需要注意的是第3个持续回溯的可能?
'''



class Solution:
    def getNextNode(self, node):
        if not node: raise ValueError
        t = node.getFirstChild()
        if t: return t
        t = node.getSibling()
        if t: return t
        t = node.getParent()
        while t:
            t = t.getSibling()
            if t: return t
            t = t.getParent()
        return