# encoding=utf-8
'''
Explain a load balancer data structure and algorithm.
'''


'''
问的是数据结构
good partition methods and hash function





We can use something like a min-heap.

Where the node value is the number of connections handled by the server.

Each server can maintain a list of clients it is serving.

In addition to this we can have a HashMap to store the <client,server> pair to retrieve the server.
'''



#关键词。server,  traffic,

'''
A load balancer is a device that acts as a reverse proxy and distributes network or application traffic across a number of servers. Load balancers are used to increase capacity (concurrent users) and reliability of applications.
'''

#果然考得是scalability相关

