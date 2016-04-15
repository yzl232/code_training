# encoding=utf-8
'''

Check for Identical BSTs without building the trees

Given two arrays which represent a sequence of keys. Imagine we make a Binary Search Tree (BST) from each array. We need to tell whether two BSTs will be identical or not without actually constructing the tree.

Examples
For example, the input arrays are {2, 4, 3, 1} and {2, 1, 4, 3} will construct the same tree

Example 1:
a[] = {2, 4, 1, 3} will construct following tree.
   2
 /  \
1    4
    /
   3
b[] = {2, 4, 3, 1} will also also construct the same tree.
   2
 /  \
1    4
    /
   3
So the output is "True"
'''

'''
a[] = {8, 3, 6, 1, 4, 7, 10, 14, 13}
b[] = {8, 10, 14, 3, 6, 4, 1, 7, 13}

sorted array : 1, 3, 4, 6, 7, 8, 10, 13, 14
elements index in array a[]: 3, 1, 4, 2, 5, 0, 6, 8, 7
elements index in array b[]: 6, 3, 5, 4, 7, 0, 1, 8, 2
'''

'''
Two arrays represent sane BST if for every element x, the elements in left and right subtrees of x appear after it in both arrays. And same is true for roots of left and right subtrees.
The idea is to check of if next smaller and greater elements are same in both arrays. Same properties are recursively checked for left and right subtrees. The idea looks simple, but implementation requires checking all conditions for all elements. Following is an interesting recursive implementation of the idea.
'''



'''
You can use the stack based approach for finding the next greater and smaller elements , and then simply compare. Complexity : O(n) for both space and time.
'''
#它给的array. 建立tree的方式：     left child == next smaller.    right child == next greater.



class Solution:
    def nge(self, arr):
        if not arr: return
        stack = []; d={}; n=len(arr)  #顺序是乱得。 用hashmap可以保存好顺序。
        for i in range(n):
            x = arr[i]
            while stack and stack[-1][0]<x:  d[stack.pop()[1]]=x  #pop出来的都是    #发现了一个比之前都要大，不断pop
            stack.append((x, i))   #存index, 以及值
        return [ None if i not in d else d[i] for i in range(n) ]


    def nse(self, arr):
        if not arr: return
        stack = []; d={}; n=len(arr)  #顺序是乱得。 用hashmap可以保存好顺序。
        for i in range(n):
            x = arr[i]
            while stack and stack[-1][0]>x:    d[stack.pop()[1]]=x  #pop出来的都是    #发现了一个比之前都要大，不断pop
            stack.append((x, i))   #存index, 以及值
        return [ None if i not in d else d[i] for i in range(n) ]

