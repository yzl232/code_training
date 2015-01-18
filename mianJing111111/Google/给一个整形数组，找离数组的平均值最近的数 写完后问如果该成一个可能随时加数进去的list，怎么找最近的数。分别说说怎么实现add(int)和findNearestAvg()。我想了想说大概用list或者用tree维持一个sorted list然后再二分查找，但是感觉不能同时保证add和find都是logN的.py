# encoding=utf-8
'''
给一个整形数组，找离数组的平均值最近的数
写完后问如果该成一个可能随时加数进去的list，怎么找最近的数。分别说说怎么实现add(int)和findNearestAvg()。我想了想说大概用list或者用tree维持一个sorted list然后再二分查找，但是感觉不能同时保证add和find都是logN的
'''


#要随时的话， 可以用 binary search tree.