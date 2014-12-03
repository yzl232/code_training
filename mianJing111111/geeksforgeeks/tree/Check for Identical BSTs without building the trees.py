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
class Solution:
    def nge(self, arr):
        if not arr: return
        stack = [arr[0]];  result = [];  d={}  #顺序是乱得。 用hashmap可以保存好顺序。
        for i in range(1, len(arr)):
            cur = arr[i]
            while stack and stack[-1]<cur: #发现了一个比之前都要大，不断pop
                d[stack.pop()]=cur  #pop出来的都是
            stack.append(cur)
        for i in arr:
            if i in d: result.append(d[i])
            else: result.append(None)  #没在hashmap的就是没有更大
        return result

    def nsr(self, arr):
        if not arr: return
        stack = [arr[0]];  result = [];  d={}  #顺序是乱得。 用hashmap可以保存好顺序。
        for i in range(1, len(arr)):
            cur = arr[i]
            while stack and stack[-1]<cur: #发现了一个比之前都要大，不断pop
                d[stack.pop()]=cur  #pop出来的都是
            stack.append(cur)
        for i in arr:
            if i in d: result.append(d[i])
            else: result.append(None)  #没在hashmap的就是没有更大
        return result
