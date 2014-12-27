# encoding=utf-8
'''
Define a class to represent a graph which supports following opertations
addEdge(Node n1,Node n2)
addNode(Object nodeData)

How do you differentiate between an edge n1->n2 and n2->n1
'''
#就是用普通的node就可以了。
class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, n1, n2):
        if n1 not in self.graph: self.graph[n1]=[]
        self.graph[n1].append(n2)

    def addNode(self, n):
        if n not in self.graph: self.graph[n]=[]