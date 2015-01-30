# encoding=utf-8
'''
Implement a Boolean vector: T, F, F, T, F, … with the following operations:
append(boolean b)
boolean get(int index)
set(int index, boolean b)
int length()
Restriction: no Java collections classes

What if you knew the vector has 99.99% T and only 0.01% False. How would you change the approach?
'''
# 第一个就是bit map.  并且动态增加array. size.   类似heap 。  不够就乘以2
# followup就是 类似稀疏矩阵。  Hashset存False的index就可以了。  set的话， 从set里边remove掉。

'''

1
For the case where we don't know in advance that most elements will be T, a good approach would be to keep a growable bitset. This is a growable array of integers, used as a bitset for space efficiency. You could write a simple ArrayList implementation that initially allocates an array of integers of some small size, and every time the array runs out of space, doubles the storage and copies the existing data over to the new storage. The i-th Boolean in the collection would be stored in the (i%32)-th bit of the (i/32)-th integer, if we assume that integers are 32-bit. This data structure has O(1) amortized add, O(1) set, and O(1) get. The space usage is O(total number of values in the collection) + O(1).





2
If we know that very few values are F and we're interested in saving space, we can keep a number to tell us how many total T and F values we have, and then keep a hash set of all the F values. To determine the value at an index, just return !hashSet.contains(index). To set an index, remove it from the hashset if setting to true; add it to the hash set if setting to false. This data structure has O(1) expected time add, set, and get. The space usage is O(number of F values) + O(1).

In both of the above implementations, the length() operation would return, in O(1) time, a previously-stored count (that is updated in O(1) time as elements are appended)
'''