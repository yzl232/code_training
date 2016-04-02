# encoding=utf-8
#关于segment tree
# https://liangsun.org/posts/a-python-implementation-of-segment-tree/
#  http://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
# 和tree差不多。。  node的值是[start, end]
#查找的时候， 如果x1==start, x2=end: 找到。
#不然比较m=(start+end )/2.  如果end< m， 在左半。  如m<start 右半。 (切较小的左半， 右半)
#  如果左右半都有。   分拆2部分，dfs后 相加

#  [xxx    m    ],  [   m  xxxx],  [   xxxxmxx       ]


# union find
'''
就是某种parent的recursion。  标记source
'''
class Solution:
    parent = {}
    def find(self, x):
        while x!=self.parent[x]:    x = self.parent[x]
        return x

    def union(self, x, y):
        r1=self.find(x); r2=self.find(y)
        self.parent[r1] = r2
        
    def add(self, x):
        self.parent[x]  = x
# 这2种数据结构少见。  只是以防万一。