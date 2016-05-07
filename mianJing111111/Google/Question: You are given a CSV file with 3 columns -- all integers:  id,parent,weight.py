# encoding=utf-8
'''
Question: You are given a CSV file with 3 columns -- all integers:

id,parent,weight
10,30,1
30,0,10
20,30,2
50,40,3
40,30,4

0 is the assumed root node with weight 0

which describes a tree-like structure -- each line is a node, 'parent' refers to 'id' of another node.

Print out, for each node, the total weight of a subtree below this node (by convention, the weight of a subtree for node X includes the own weight of X).

You may assume that the input comes pre-parsed as a sequence of Node objects
(substitute the appropriate syntax for java/python/c++):

Node {
int id;
int parent;
int weight;
// ... you can add other fields right here, if necessary
}

implement the following:
public void printSubTreeWeight(List<Node> nodes) {
....}
'''
#比较适合用memoization来做。
#dp不大好操作。

# 又是build tree。  建图。 找root。  BFS。


# undirected graph.   适合union find。   其他不适合。

class Solution:  #可以用hashmap  build 简单的node: children属性。   #也就是hashtable based..    tree
    def buildTree(self, relations):
        d = {};  notRoot = set()
        for rs in relations:
            if d[rs[0]] not in d:  d[rs[0]] = []
            d[rs[0]].append(rs[1])
            notRoot.add(rs[1])
        roots=[]    #找root
        for k in d.keys():
            if k not in notRoot:  roots.append(k)



# 第二部分。 更新为sum of decendents
    def dfs(self, root):
        for x in root.children:   root.val +=self.dfs(x)
        return root.val


'''
class Solution:
    def calWeights(self, triples):
        tree = {t[0]:[] for t in triples};  weights={t[1]:0 for t in triples}
        for t in triples:
            tree[t[1]].append(t[0])
            weights[t[0]] = t[2]
        self.subTreeW={}; self.weights = weights; self.tree = tree
        for t in triples:  self.dfs(t[0])
        return self.subTreeW

    def dfs(self, id):
        if id in self.subTreeW: return self.subTreeW[id]
        w = self.weights[id]
        for child in self.tree[id]:  #直到dfs到child为空的为止。
            w+=self.dfs(child)
        self.subTreeW[id] = w
'''