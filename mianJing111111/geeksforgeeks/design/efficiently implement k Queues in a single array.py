# encoding=utf-8
'''

How to efficiently implement k Queues in a single array?

We have discussed efficient implementation of k stack in an array. In this post, same for queue is discussed. Following is the detailed problem statement.


Create a data structure kQueues that represents k queues. Implementation of kQueues should use only one array, i.e., k queues should use the same array for storing elements. Following functions must be supported by kQueues.

enqueue(int x, int qn) –> adds x to queue number ‘qn’ where qn is from 0 to k-1
dequeue(int qn) –> deletes an element from queue number ‘qn’ where qn is from 0 to k-1




Method 2 (A space efficient implementation)
The idea is similar to the stack post, here we need to use three extra arrays. In stack post, we needed to extra arrays, one more array is required because in queues, enqueue() and dequeue() operations are done at different ends.

Following are the three extra arrays are used:
1) front[]: This is of size k and stores indexes of front elements in all queues.   队列首
2) rear[]: This is of size k and stores indexes of rear elements in all queues.   队列尾
2) next[]: This is of size n and stores indexes of next item for all items in array arr[].   下一个元素index

Here arr[] is actual array that stores k stacks.

Together with k queues, a stack of free slots in arr[] is also maintained. The top of this stack is stored in a variable ‘free’.

All entries in front[] are initialized as -1 to indicate that all queues are empty. All entries next[i] are initialized as i+1 because all slots are free initially and pointing to next slot. Top of free stack, ‘free’ is initialized as 0.
'''