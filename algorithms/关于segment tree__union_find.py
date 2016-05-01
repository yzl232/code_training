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
    def solve(self, n):
        parent = range(n)
        def find(x):
            if x!=parent[x]: parent[x] = find(parent[x])  #路径压缩
            return parent[x]

        def union( x, y):      #parent[find(x)] = find(y)  如果只是这一句 ， 不需要定义union函数。
            a,  b = find(x), find(y)
            parent[a] = b
            return True if a!=b else False
            