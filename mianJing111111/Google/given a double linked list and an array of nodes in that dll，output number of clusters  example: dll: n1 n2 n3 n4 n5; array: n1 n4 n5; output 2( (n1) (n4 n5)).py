# encoding=utf-8
'''
given a double linked list and an array of nodes in that dll，output number of clusters
example: dll: n1 n2 n3 n4 n5;
array: n1 n4 n5;
output 2( (n1) (n4 n5))
'''
#最多是len(array) 个。 如果黏在一起，就不是了。


'''
题目觉得不难  但是脑子很不给力  想了好半天也没想好  发出来大家看看

给一个
class Node{
   public Node next();
}
就是说你不能修改这个list

一个list， A->B->C->D->E->F->G->........->Z (当然这只是个例子  list 无序)
给几个 list中的nodes, C, A, B, E, G
求 cluster 的个数
Cluster1: A->B->C
Cluster2: E
Cluster3: G
所以三个

然后要考虑 list size 为 1M   node数量为10 的情况, 也就是说你牛别给我iterate
list了


【 在 livbai (梦想人生) 的大作中提到: 】
: 一个hashtable，每个node过一次，看看有几个node.next不存在。
'''



#每个node过一次，看看有几个node.next不存在。
#有点像leetcode的一道用hashmap找consecutive的题目.
#理解了以后，就几行代码
#甚至都不需要head node
class Solution:
    def findC(self, arr):
        ret = 0; targets = {i:False for i in arr}
        for i in targets:
            if i.next not in targets: ret+=1
        return ret


'''
暴力法，比较烂
class Solution:
    def getNumCluster(self, node, arr):
        d = {i:1 for i in arr}
        n = len(arr)     #array里边的。
        prevInD = False
        result = 0
        while n>0 and node:
            if node in d:
                n-=1
                if not prevInD: result+=1
                prevInD = True
            else:  prevInD = False
            node = node.next
        return result
'''
