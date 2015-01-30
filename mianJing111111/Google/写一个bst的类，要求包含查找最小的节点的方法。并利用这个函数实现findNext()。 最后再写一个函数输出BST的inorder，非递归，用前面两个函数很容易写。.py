# encoding=utf-8
'''
写一个bst的类，要求包含查找最小的节点的方法。并利用这个函数实现findNext()。
最后再写一个函数输出BST的inorder，非递归，用前面两个函数很容易写。
'''


# 最小的函数。  while root.left: root = root.left
#  findNext:  root.right, 然后left most node.

# in-order .  stack