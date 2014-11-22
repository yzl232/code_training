# encoding=utf-8
'''
给一个sequence，里面有很多数字，顺序很乱，也有重复，例如：

9,8,3,8,8,5,2,9........

找出这串数字中长度为‘k’的subsequence（不是subarray, 我专门问了，就是subsequence，不一定挨着的元素序列），使得这串subsequence的和最大。


本质上就是就是求前k个元素

用既然是0~9quick select找到前k个。 然后求和
'''


'''
给一个词典[Foo, Fo, Bar], k  ]3 N+ B+ W# d( [

给一个word，要求实现一个方法来表示这个词在词典中存在。
这个word是可以有wildcard的例如
"F*o" => true
"**r" => true4

做法就是建立trie。  碰到*， 就考虑iterate  所有子树，dfs。

'''

'''
Return a list of the averages of each level of the tree

注意存下count, sum就好。
iterative更合适一些。
'''