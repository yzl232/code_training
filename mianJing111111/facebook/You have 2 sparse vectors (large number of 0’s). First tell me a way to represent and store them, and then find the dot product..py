# encoding=utf-8
'''
You have 2 sparse vectors (large number of 0’s). First tell me a way to represent and store them, and then find the dot product.
'''
#(To store them, we should store the value and index of those indexes that have a non-zero value, and then finding the dot product is very straight forward).



'''
 How to do a dot product (or other operations) on very very  big vectors? (migh be very sparse and of unequal lenghts) Data structures with discution, clean algorithm, extensible if some relations are known.
'''

#  www.cs.uiuc.edu/class/fa07/cs498mjg/notes/sparsity.pdf


#对于sparse matrix:  保存为[（val, row, col）, (val2, row2, col2), ......    ]
#或者 val,  col, row 3个array



'''

You are given 2 streams of data, representing very sparse vectors
you are guaranteed that the 2 incoming streams are of same size
give a data structure which is optimized for producing the dot product of those sparse vectors
analyze your runtime/space complexity,
b) what if you are now told that v1, is much more sparse than v2
give another (or the same) data structure optimized for the dot product of any such 2 vectors (where 1 is more sparse than the other)
'''


#facebook这道题目。 可以这样。只储存非0的value.    (val, index). sort by index
class Solution:  #  (val, index).
    def multip(self, v1, v2):
        ret =[];  i=j=0
        while i<len(v1) and j<len(v2):
            x1, x2 = v1[i][-1], v2[j][-1]
            if x1==x2:    ret.append(   (v1[i][0]*v2[j][0], x1  )    )
            elif x1<x2:  i+=1
            else: j+=1
        return ret
