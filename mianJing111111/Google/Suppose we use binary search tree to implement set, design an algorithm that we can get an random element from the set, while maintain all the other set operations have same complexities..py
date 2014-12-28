# encoding=utf-8
'''
Suppose we use binary search tree to implement set, design an algorithm that we can get an random element from the set, while maintain all the other set operations have same complexities.
'''


'''
Here is my thought: all we need is an API which will find the kth element in the tree, such as tree.find(int k). For the kth element, we can achieve O(n) time complexity using normal binary search tree itself. If we want better, we can store some counts of child elements in the node, and so the delete and insert operation would need to update the count of all its Ancestors. The final performance of search would depend on the snap shot of tree at the time. If it is more like balanced binary search tree, you got the O(log(n)). If it is more like a list, it is O(n). But it will all guarantee the uniform probability distribution at any snapshot of the tree.
'''

