# encoding=utf-8
'''

Next Greater Element
正数哈
Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.

Examples:
a) For any array, rightmost element always has next greater element as None.
b) For an array which is sorted in decreasing order, all elements have next greater element as None.
c) For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.

Element       NGE
   4      -->   5
   5      -->   25
   2      -->   25
   25     -->   None

'''
#O(n)
'''
Method 2 (Using Stack)
Thanks to pchild for suggesting following approach.
1) Push the first element to stack.
2) Pick rest of the elements one by one and follow following steps in loop.
….a) Mark the current element as next.
….b) If stack is not empty, then pop an element from stack and compare it with next.
….c) If next is greater than the popped element, then next is the next greater element for the popped element.
….d) Keep poppoing from the stack while the popped element is smaller than next. next becomes the next greater element for all such popped elements
….g) If next is smaller than the popped element, then push the popped element back.
3) After the loop in step 2 is over, pop all the elements from stack and print -1 as next element for them.
'''
#O(n)    比较难。 不大懂    背下.  才10行代码。  循环里就2行。
class Solution:    #存的是tuple   (val, i)
    def nge(self, arr):
        if not arr: return
        stack = []; d={}; n=len(arr)  #顺序是乱得。 用hashmap可以保存好顺序。
        for i in range(n):    #发现了一个比之前都要大，不断pop
            while stack and stack[-1][0]<arr[i]:    d[stack.pop()[1]]=arr[i]  #pop出来的都是
            stack.append((arr[i], i))           #存index, 以及值
        ret = [None]*n
        for i in range(n):
            if i in d:  ret[i]=d[i]
        return ret
s = Solution()
print s.nge([4, 2, 5,6, 2, 4])
print s.nge([11, 13, 21, 3])
print s.nge([ 9, 2, 1, 4, 8])
print s.nge([2, 4, 5, 2, 9])
# 如果求next greatest。 就是从右边往左dp