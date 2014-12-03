# encoding=utf-8
'''
Given a self-balancing tree (AVL), code a method that returns the median.(Median: the numerical value separating the higher half of a data sample from the lower half. Example: if the series is

2, 7, 4, 9, 1, 5, 8, 3, 6

then the median is 5.)
'''
'''
Create the data structure for a component that will receive a series of numbers over the time and, when asked, returns the median of all received elements.

(Median: the numerical value separating the higher half of a data sample from the lower half. Example: if the series is

2, 7, 4, 9, 1, 5, 8, 3, 6

then the median is 5.)

Model the data structure for a component that would have these two methods:

@interface SampleHandler {
- (void)addNumber:(NSNumber*)number;
- (NSNumber*)median;
}

Justify your decisions. Calculate the complexity of each method.
'''


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



Method 2: Augmented self balanced binary search tree (AVL, RB, etc…)

At every node of BST, maintain number of elements in the subtree rooted at that node. We can use a node as root of simple binary tree, whose left child is self balancing BST with elements less than root and right child is self balancing BST with elements greater than root. The root element always holds effective median.

If left and right subtrees contain same number of elements, root node holds average of left and right subtree root data. Otherwise, root contains same data as the root of subtree which is having more elements. After processing an incoming element, the left and right subtrees (BST) are differed utmost by 1.

这一句很巧妙。 root==   较大的子树的root的val。   或者是平均左右子树的root


Self balancing BST is costly in managing balancing factor of BST. However, they provide sorted data which we don’t need. We need median only. The next method make use of Heaps to trace median.

Method 3: Heaps






Similar to balancing BST in Method 2 above, we can use a max heap on left side to represent elements that are less than effective median, and a min heap on right side to represent elements that are greater than effective median.

After processing an incoming element, the number of elements in heaps differ utmost by 1 element. When both heaps contain same number of elements, we pick average of heaps root data as effective median. When the heaps are not balanced, we select effective median from the root of heap containing more elements.

Given below is implementation of above method. For algorithm to build these heaps, please read the highlighted code.

'''



'''
We need to maintain 1 max heap and 1 min heap. Max heap will contain lower half of the numbers and min the upper half. Whenever, a new number comes:
1) if its less than root of max heap, it is inserted into max heap.
2) if its higher than root of min heap, it is inserted into min heap.
3) after insertion if the size difference of two heaps is greater than 1, the root of the larger heap is transferred to the other heap to balance their size.

At any point, the median will be:
1) (root of max heap + root of min heap) / 2 if size of both heap are equal.
2) root of larger heap otherwise.
'''