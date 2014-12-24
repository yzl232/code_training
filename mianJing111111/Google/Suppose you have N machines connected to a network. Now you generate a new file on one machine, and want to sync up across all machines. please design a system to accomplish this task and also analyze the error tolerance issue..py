# encoding=utf-8
'''
Suppose you have N machines connected to a network.
Now you generate a new file on one machine, and want to sync up across all machines. please design a system to accomplish this task and also analyze the error tolerance issue.
'''


'''
We had this problem at the office. The best way to do it is to order your nodes as a binary tree (a heap representation will do)

Node1
Node2      Node3
Node4 Node5 Node6 Node7

at T-0 Node1 pases the data to Node2, at T-1 Node1 passes data to Node3 and Node2 passes data to Node4, at T-3 Node2 passes data to Node5, Node3 passes data to Node6, at T-4 Node3 passes data to Node7.

There's even an optimization in which not all data is passed in each step but just chucks, and when each node has a chunk, they start passing them to the next node. That reduces vastly the amount of data passed in the network at each step reducing congestion and augmenting throughput. The only problem is I cannot remember the optimization but is based on how OpenMPI implements MPI_Bcast.
'''



'''
wouldn't that cause retransmission, how about divide file into smaller fixed size segments then main computer uses UDP datagram and broadcast each segment along with sequential incrementing id. Once all packets done transmission clients may ask for missing segment, and it can retransmit.
'''