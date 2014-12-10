# encoding=utf-8
'''
Given an N-ary tree where every node has at-most N children. How to serialize and deserialze it? Serialization is to store tree in a file so that it can be later restored. The structure of tree must be maintained. Deserialization is reading tree back from file.


The idea is to store an ‘end of children’ marker with every node. The following diagram shows serialization where ‘)’ is used as end of children marker.

http://www.geeksforgeeks.org/serialize-deserialize-n-ary-tree/
'''
N =5

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution1:
    def serialize(self, root):
        self.result = []
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:   return   #不能在这里append '#'。因为for loop。 几乎不会 not root
        self.result.append(root.val)
        for c in root.children:
            self.dfs(c)
        self.result.append('#')

class Solution:
    def deSerialize(self, arr):
        self.index = 0; self.arr = arr
        return self.dfs()

    def dfs(self):
        if self.index>=len(self.arr): return
        rootVal = self.arr[self.index]
        if rootVal == '#':
            self.index+=1
            return
        else:
            root = TreeNode(rootVal)
            self.index+=1
            while True:    #这里和binary不同
                tmp = self.dfs()
                if not tmp: break
                root.children.append(tmp)
            return root
t = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)
t3 = TreeNode(4)
t.children+=[t1, t2, t3]
s = Solution1()
aaa = s.serialize(t)
print aaa
s2 = Solution()
root = s2.deSerialize(aaa)
print s.serialize(root)