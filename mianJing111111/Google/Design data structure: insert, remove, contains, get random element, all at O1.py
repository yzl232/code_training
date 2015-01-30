# encoding=utf-8
'''
#G家超超高频的题目

Data structure: insert, remove, contains, get random element, all at O(1)

Consider a data structure composed of a hashtable H and an array A. The hashtable keys are the elements in the data structure, and the values are their positions in the array.
hashtable key是值，  val保存pointer 到array得位置(index)。  array保存的是val。
insert:  插入到array。 append
remove:  hash找到。 然后找到pointer。 然后用最后一个数替代。然后减小array size。 del hashtable,  更新最后一个数在hashtable的位置
contain:  hash表
 get  random:   random()%size.      array里面保存的是值。 也就是hashtable的key。

# 如果考虑重复的值。 那么hashtable key仍然是值。 val存的是 [index1,  index2 ,  ...]
    insert(value): append the value to array and let i be it's index in A. Set H[value]=i.
    remove(value): 这个替代很巧妙。
    We are going to replace the cell that contains value in A with the last element in A.
    let d be the last element in the array A at index m.

    let i be H[value],
    the index in the array of the value to be removed. Set A[i]=d, H[d]=i,
    decrease the size of the array by one, and remove value from H.

    contains(value): return H.contains(value)

    getRandomElement(): let r=random(current size of A). return A[r].
'''



'''
Use an array to store the elements of the set, and a hash table to store a list of (key,value) pairs, where the keys are elements of the set, and the values are the array indices for the keys. For convenience, we also store the size of the set.

add(p):
   if p is already a key in hash table, return
   array[size]=p \\move array if overflow
   add p:size to the hash table
   size++

delete(p):
   i = value stored in hash table with key p
   size--
   array[i]=array[size]
   update the value in hash table with key array[i] to i \\Thanks, anon.
   delete the key p from the hash table

get_random():
   return array[randrange(0,size)]

The function randrange(x,y) is assumed to return a random integer in the interval [x,y).

This has amortized O(1) time for all three functions.
'''


# RF居然考G家的题目


'''
换汤不换药。  G家又考了一次
Implementation of Advanced set which have the functionality as "Set" in c++ along with extra functionality-Random number generator.Returns the random number from the set.
'''