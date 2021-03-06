# encoding=utf-8
'''
We have a list of N nodes with each node pointing to one of the N nodes.
It could even be pointing to itself. We call a node ‘good’,
if it satisfies one of the following properties:

* It is the tail node (marked as node 1)
* It is pointing to the tail node (node 1)
* It is pointing to a good node

You can change the pointers of some nodes in order to make them all ‘good’.
You are given the description of the nodes.
You have to find out what is minimum number of nodes that you have to change in order
to make all the nodes good.

Input:
The first line of input contains an integer number N which is the number of nodes.
The next N lines contains N numbers,
all between 1 and N.
The first number, is the number of the node pointed to by Node 1;
the second number is the number of the node pointed to by Node 2;
the third number is the number of the node pointed to by Node 3 and so on.

N is no larger than 1000.

Output:
Print a single integer which is the answer to the problem

Sample Input 1:
5
1
2
3
4
5

Sample output 1:
4

Explanation:
We have to change pointers for four nodes (node #2 to node #5) to point to node #1.
Thus 4 changes are required

Sample input 2:
5
5
5
5
5
5

Sample output 2:
1

Explanation:
We have to just change node #5 to point to node #1 (tail node) which will make node #5 good.
Since all the other nodes point to a good node (node #5), every node becomes a good node.
'''

'''
1. Remove the edge (pointer) from 1.
2. Find connected components.
3. The answer is the number of connected components - 1 (i.e. all the connected components except for the one that contains 1).
'''

'''
#基本上是用recursion。  当指向自己的时候。 停止recursion.




class Solution:
    def find_root(self, arr, x):
        if x in self.d: return self.d[x]  # memoization
        if x==arr[x]:          #while arr[x]!=x:  x=arr[x]
            self.d[x]=x
            return x
        self.d[x]= self.find_root(arr, arr[x])
        return self.d[x]

    def count_max_nodes(self, arr):
        arr=[x-1 for x in arr] #变成0 based array
        self.d={}
        for i in range(1,len(arr)):   self.find_root(arr,i)
        return len(set(self.d.values()))
s = Solution()
print s.count_max_nodes([1,2,3,4,5])
print s.count_max_nodes([5,5,5,5,5])
print s.count_max_nodes([1,5,1,2,5])
'''
#要么输入不valid,  死循环 。  要么最坏情况 n2 .  因为arr[i]==i  停止 。 所以每次recursion最多n次
#dfs加上一个visited的hashmap， 可以检查invalid  死循环

# 有点像并查集
# 。
#用memoization是最优化的。
#绝对是并查集了..
class Solution:
    def solve(self, arr):
        parent = {x:i for i,x in enumerate(arr[1:])}
        def find(x):
            if x!=parent[x]: parent[x] = find(parent[x])
            return parent[x]
        for i,x in enumerate(arr[1:]):  find(x)
        t = set(parent.values())
        return len(t) if 1 not in t else len(t)-1
'''
class Solution:
    def find_root(self, arr, x):
        while arr[x]!=x:  x=arr[x]
        return x

    def count_max_nodes(self, arr):
        arr=[x-1 for x in arr] #变成0 based array
        self.d={}
        for i in range(1,len(arr)):
            arr[i] = self.find_root(arr,i)
        return len(set(arr))
'''
s = Solution()
print s.count_max_nodes([1,2,3,4,5])
print s.count_max_nodes([5,5,5,5,5])
print s.count_max_nodes([1,5,1,2,5])


# 类似于union find 。  也类似于build  tree
# 也可以用BFS。
#不过还是最适合union find

s = Solution()
print s.count_max_nodes([1,2,3,4,5])
print s.count_max_nodes([5,5,5,5,5])
print s.count_max_nodes([1,5,1,2,5])