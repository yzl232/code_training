# encoding=utf-8
'''
电面：
一个数组 A: 1 3 0 2 4
input: dest-node: A0
output: all the source nodes: (A1, A3, A4)

数组中每个元素表示他能走的步数，技能向左走 又能向右走，能到A[0]的点有A[1]和A[4]，A[1]可以走3步到A[4] A[4]能走4步道A[0]。
输出所有能到A[0]的index。
'''
#水题目
class Solution:
    def find(self, arr, dest):
        ret = []
        for i in range(len(arr)):
            if i==dest: continue
            if i<dest and i+arr[i]>=dest: ret.append(i)
            if i>dest and i-arr[i]<=dest: ret.append(i)
        return ret