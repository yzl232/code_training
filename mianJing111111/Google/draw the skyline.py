# encoding=utf-8
'''
draw the skyline
一堆interval，带有start和end，以及高度，整合之后， 请输出每个时间段及这个时
间段内最大的高度。

Example Input：
S1: {[2,5], vol=10}, {[6,10], vol=2}
S2: {[1,6], vol=1}, {[8,12], vol=8}

Example Output:
[1,2],vol=1, [2,5], vol=10, [5,6], vol = 1, [6,8], vol = 2, [8,12], vol = 8.

 {[2,5], vol=10}
rectangle(2, 5, 10)


http://www.mitbbs.com/article_t/JobHunting/32809753.html
'''

'''
一个先将endpoint排序，另外用一个BST维护当前的最大高度，然后结束时就删除相应
的节点，这个感觉很难想，代码简洁一点。


碰到start point就放入。 碰到end  point就删除。  保持一个 binay search tree
可以加上一个hashtable。

用ordered dict。  可以的。

'''
