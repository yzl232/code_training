# encoding=utf-8
# 数组中每个元素表示他能走的步数，技能向左走 又能向右走，能到A[0]的点有A[1]和A[4]
'''
电面：
一个数组 A: 1 3 0 2 4 7  1
input: dest-node: A0
output: all the source nodes: (A1, A3, A4)

数组中每个元素表示他能走的步数，技能向左走 又能向右走，能到A[0]的点有A[1]和A[4]，A[1]可以走3步到A[4] A[4]能走4步道A[0]。
输出所有能到A[0]的index。
'''


#  不是leetcode能到达最远那道题，这里面只能走这些步数，而且可以多跳跳到也算
#  只要看出是个图就是水水的了
#  可以理解为反着建图。。。就是临接表（反向） 每个位置存 能到它的所有位置
class Solution:
    def solve(self, arr):
        n = len(arr)
        graph = {i: [] for i in range(n)}
        for i in range(n):
            if 0<=i-arr[i]<n:  graph[i-arr[i]].append(i)
            if 0<=i+arr[i]<n:  graph[i+arr[i]].append(i)  #建图。
        pre = set([0])  # BFS
        ret = set([]);   visited = set([0])
        while pre:
            cur = set([])
            for x in pre:
                for y in graph[x]:
                    if y in visited: continue
                    visited.add(y)
                    cur.add(y)
            ret.update(cur)
            pre = cur
        return ret
s = Solution()
print s.solve([1, 3, 0, 2, 4, 7, 1])