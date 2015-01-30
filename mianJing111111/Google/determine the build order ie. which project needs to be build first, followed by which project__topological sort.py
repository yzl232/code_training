# encoding=utf-8
'''
G家面试题
You are given a text file that has list of dependencies between (any) two projects in the soure code repository. Write an algorithm to determine the build order ie. which project needs to be build first, followed by which project..based on the dependencies.
Bonus point: If you can detect any circular dependencies and throw an exception if found.

EX: ProjectDependencies.txt
a -> b (means 'a' depends on 'b'..so 'b' needs to be built first and then 'a')
b -> c
b -> d
c -> d
##依赖性。  尖头表示依赖。 所以先解决箭头右边的。
Then the build order can be

d , c, b, a in that order



In DFS, we start from a vertex, we first print it and then recursively call DFS for its adjacent vertices. In topological sorting, we use a temporary stack. We don’t print the vertex immediately, we first recursively call topological sorting for all its adjacent vertices, then push it to a stack. Finally, print contents of stack. Note that a vertex is pushed to stack only when all of its adjacent vertices (and their adjacent vertices and so on) are already in stack.

'''



##as pairs of nodes and their outgoing edges:   节点和出去的节点。

##
'''
 Topological Sort
Topological Sorting
Sandro is a well organised person. Every day he makes a list of things which need to be done and enumerates them from 1 to n. However, some things need to be done before others. In this task you have to find out whether Sandro can solve all his duties and if so, print the correct order.

Input
In the first line you are given an integer n and m (1<=n<=10000, 1<=m<=1000000). On the next m lines there are two distinct integers x and y, (1<=x,y<=10000) describing that job x needs to be done before job y.

Output
Print "Sandro fails." if Sandro cannot complete all his duties on the list. If there is a solution print the correct ordering, the jobs to be done separated by a whitespace. If there are multiple solutions print the one, whose first number is smallest, if there are still multiple solutions, print the one whose second number is smallest, and so on.

Example 1

Input:
8 9
1 4
1 2
4 2
4 3
3 2
5 2
3 5
8 2
8 6
Output:
1 4 3 5 7 8 2 6


Example 2

Input:
2 2
1 2
2 1
Output:
Sandro fails.


'''



# Simple:
# a --> b
#   --> c --> d
#   --> d
graph1 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d"],
    "d": []
}

# 2 components
graph2 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d"],
    "d": [],
    "e": ["g", "f", "q"],
    "g": [],
    "f": [],
    "q": []
}

# cycle
graph3 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d", "e"],
    "d": [],
    "e": ["g", "f", "q"],
    "g": ["c"],
    "f": [],
    "q": []
}

#基本上就是DFS而已。 10几行。

class Solution:
    def topological(self, graph):   # 按题目输入，应当建一个hashmap.:    fromD = {}
        self.graph = graph
        self.ret,  self.visited = [], {}  # visited最开始为空。
        for k in graph:  self.dfs(k)
        return self.ret
    def dfs(self, x):
        if x in self.visited:   #已经visit过了
            if self.visited[x]==False: raise ValueError("cycle")  #发现了一个back edge。
            return
        self.visited[x] = False  #这就是与普通dfs的唯一不同。 用False标记
        for y in self.graph[x]:  self.dfs(y)
        self.ret.append(x)
        self.visited[x] = True

s = Solution()
# check how it works
print s.topological(graph1)
print s.topological(graph2)
s.topological(graph3)



'''

#http://blog.jupo.org/2012/04/06/topological-sorting-acyclic-directed-graphs/
#而且代码其实比较短。 可以背下。
#实际上是O(n2).  用DFS可以做到 O(V)+O(E)
def topolgical_sort(graph_unsorted):
    graph_sorted = []
    graph_unsorted = dict(graph_unsorted)
    while graph_unsorted:
        hasCycle = True
        for node, neighbours in graph_unsorted.items(): #这里用了items()。 后面可以自由修改graph。。相当于array[:]
            for n in neighbours:
                if  n in graph_unsorted:
                    break  #有一个依赖。不用管了。下一个。
            else:  #所有的都不在unsorted。说明没有依赖了。 可以使用。
                hasCycle = False
                del graph_unsorted[node]
                graph_sorted.append((node, neighbours))
        if hasCycle:        #每次都要检查有没有环。
            raise RuntimeError("A cyclic dependency occurred")
    return graph_sorted

#依赖最少的排在前面
graph_unsorted = [(2, []),
                  (5, [11]),
                  (11, [2, 9, 10]),
                  (7, [11, 8]),
                  (9, []),
                  (10, []),
                  (8, [9]),
                  (3, [10, 8])]
print topolgical_sort(graph_unsorted)



'''