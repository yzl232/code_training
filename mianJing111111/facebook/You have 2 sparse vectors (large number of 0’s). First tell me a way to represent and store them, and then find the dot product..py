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



#facebook这道题目。 可以这样。只储存非0的value.    (val, index). sort by index
class Solution:
    def multip(self, v1, v2):
        result =[]
        i=j=0
        while i<len(v1) and j<len(v2):
            if v1[i][-1]==v2[j][-1]:
                result.append(   (v1[i][0]*v2[j][0], v1[i][-1]   )    )
            elif v1[i][-1]<v2[j][-1]:
                i+=1
            else: j+=1
        return result
