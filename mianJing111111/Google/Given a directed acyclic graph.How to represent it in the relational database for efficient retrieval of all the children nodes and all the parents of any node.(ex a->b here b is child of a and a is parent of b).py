# encoding=utf-8
'''
Given a directed acyclic graph.How to represent it in the relational database for efficient retrieval of all the children nodes and all the parents of any node.(ex a->b here b is child of a and a is parent of b)
'''

'''
This is a pretty general solution:

Table Nodes
(Node_ID INT, Node_Value X)
Table Adjacents
(Node_ID INT, Adj_Node_ID INT)

Then to retrieve all children of a node:
Select Adj_Node_ID from Adjacents Where Node_ID=SomeNodeId

To retrieve the 'parents' of a node:
Select Node_ID from Adjacents Where Adj_Node_ID=SomeNodeId
'''