# encoding=utf-8
'''

不用写代码。
Median in a stream of integers (running integers)

Given that integers are read from a data stream. Find median of elements read so for in efficient way. For simplicity assume there are no duplicates. For example, let us consider the stream 5, 15, 1, 3 …

After reading 1st element of stream - 5 -> median - 5
After reading 2nd element of stream - 5, 15 -> median - 10
After reading 3rd element of stream - 5, 15, 1 -> median - 5
After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on...

Making it clear, when the input size is odd, we take the middle element of sorted data. If the input size is even, we pick average of middle two elements in sorted stream.

Note that output is effective median of integers read from the stream so far. Such an algorithm is called online algorithm. Any algorithm that can guarantee output of i-elements after processing i-th element, is said to be online algorithm. Let us discuss three solutions for the above problem.


BST加上一个size （AVL tree）
Method 2: Augmented self balanced binary search tree (AVL, RB, etc…)  （BST====）

At every node of BST, maintain number of elements in the subtree rooted at that node. We can use a node as root of simple binary tree, whose left child is self balancing BST with elements less than root and right child is self balancing BST with elements greater than root. The root element always holds effective median.

If left and right subtrees contain same number of elements, root node holds average of left and right subtree root data. Otherwise, root contains same data as the root of subtree which is having more elements. After processing an incoming element, the left and right subtrees (BST) are differed utmost by 1.

Self balancing BST is costly in managing balancing factor of BST. However, they provide sorted data which we don’t need. We need median only. The next method make use of Heaps to trace median.

Method 3: Heaps






Similar to balancing BST in Method 2 above, we can use a max heap on left side to represent elements that are less than effective median, and a min heap on right side to represent elements that are greater than effective median.

After processing an incoming element, the number of elements in heaps differ utmost by 1 element. When both heaps contain same number of elements, we pick average of heaps root data as effective median. When the heaps are not balanced, we select effective median from the root of heap containing more elements.

Given below is implementation of above method. For algorithm to build these heaps, please read the highlighted code.

'''



'''
We need to maintain 1 max heap and 1 min heap. 

Max heap will contain lower half of the numbers and min the upper half. 

maxHeap存较小的一半。  minHeap存较大的一半。  很容易记忆。 相反。

如果大于minHeap Min,存进去。
else： 村左边

if size相差大于2：  平衡一下

Whenever, a new number comes:
1) if its less than root of max heap, it is inserted into max heap.
2) if its higher than root of min heap, it is inserted into min heap.
3) after insertion if the size difference of two heaps is greater than 1, the root of the larger heap is transferred to the other heap to balance their size.

At any point, the median will be:
1) (root of max heap + root of min heap) / 2 if size of both heap are equal.
2) root of larger heap otherwise.
'''