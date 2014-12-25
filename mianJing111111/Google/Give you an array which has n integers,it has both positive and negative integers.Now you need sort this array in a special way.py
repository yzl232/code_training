# encoding=utf-8
'''
Give you an array which has n integers,it has both positive and negative integers.Now you need sort this array in a special way.After that,the negative integers should in the front,and the positive integers should in the back.Also the relative position should not be changed.
eg. -1 1 3 -2 2 ans: -1 -2 1 3 2.
'''
#不用保持order就好办。  sort color
#保持order    用O(n) space。  分成2个array