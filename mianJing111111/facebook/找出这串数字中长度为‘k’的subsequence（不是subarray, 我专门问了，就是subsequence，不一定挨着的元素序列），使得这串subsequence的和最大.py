# encoding=utf-8
'''
 给一个sequence，里面有很多数字，顺序很乱，也有重复，例如：

9,8,3,8,8,5,2,9........

找出这串数字中长度为‘k’的subsequence（不是subarray, 我专门问了，就是subsequence，不一定挨着的元素序列），使得这串subsequence的和最大。

实际上是求最大的k个数。  因为不是increasing sequenc这种限制。 就是任意了。  用quick select做。
'''