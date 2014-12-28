# encoding=utf-8
'''
Data-structure and algorithm used in Load Balancer
'''

'''
We can use something like a min-heap.

Where the node value is the number of connections handled by the server.

Each server can maintain a list of clients it is serving.

In addition to this we can have a HashMap to store the <client,server> pair to retrieve the server.
'''