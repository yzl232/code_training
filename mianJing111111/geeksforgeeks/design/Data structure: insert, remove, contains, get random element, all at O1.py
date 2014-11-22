# encoding=utf-8
'''

Data structure: insert, remove, contains, get random element, all at O(1)

Consider a data structure composed of a hashtable H and an array A. The hashtable keys are the elements in the data structure, and the values are their positions in the array.
hashtable保存pointer 到array得位置。  array保存的时key。
insert:  插入到array。 append
remove:  hash找到。 然后找到pointer。 然后用最后一个数替代。然后减小array size
contain:  hash表
 get  random:   random()%size.      array里面保存的是key。


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
