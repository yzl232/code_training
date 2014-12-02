# encoding=utf-8
'''

Rearrange positive and negative numbers in O(n) time and O(1) extra space

An array contains both positive and negative numbers in random order. Rearrange the array elements so that positive and negative numbers are placed alternatively. Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9], then the output should be [9, -7, 8, -3, 5, -1, 2, 4, 6]



The solution is to first separate positive and negative numbers using partition process of QuickSort. In the partition process, consider 0 as value of pivot element so that all negative numbers are placed before positive numbers. Once negative and positive numbers are separated, we start from the first negative number and first positive number, and swap every alternate negative number with next positive number.
'''








'''



挺垃圾的。 艹。 O（n2）  我觉得不会考。  它说保持相对顺序。 负数，正数。

别看了。  如果要O(n) time。  简单的用2个array。

Rearrange array in alternating positive & negative items with O(1) extra space
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance.
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

Example:

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}



posi = [x for x in a inf x<0]
nega = [x for x in a inf y<0]

然后合并。

space O(1). time O(n2)
奇数index, 偶数index
An element is out of place if it is negative and at odd index, or it is positive and at even index.

// find the item which must be moved into the out-of-place
            // entry if out-of-place entry is positive and current
            // entry is negative OR if out-of-place entry is negative
            // and current entry is negative then right rotate
            //
            // [...-3, -4, -5, 6...] -->   [...6, -3, -4, -5...]
            //      ^                          ^
            //      |                          |
            //     outofplace      -->      outofplace
            //

        time: space:  O(n)的做法。 开2个新arr，一个存负数。一个存正数。
     O(n^2) , O(1)
'''

class Solution:
    def rightRotate(self, arr, outofplace, cur):
        tmp = arr[cur]
        for i in range(cur, outofplace, -1):
            arr[i] = arr[i-1]
        arr[outofplace] = tmp


#比google的题目复杂
    def reaggrange(self, arr):
        outOfPlace = -1
        for i in range(0, len(arr)):
            if outOfPlace>=0:
                if (arr[i]>=0)  ^ (arr[outOfPlace]>=0) :#正负符号不同  #(arr[i]>=0 and arr[outOfPlace]<0) or (arr[i]<0 and arr[outOfPlace]>=0):
                    self.rightRotate(arr, outOfPlace, i)
                    print arr
                    if i-outOfPlace>2:  #刚刚搞定一个。下一个可能就是n+2
                        outOfPlace+=2
                    else:  outOfPlace=-1  #没有。。
            if outOfPlace==-1:
                if (arr[i]>=0) ^ (i%2==0):   #无法理解可以举特例。 i=0... 都满足，正常。i=1...都不满足。正常。
                    outOfPlace = i   # 正数本来在奇数位的。。
        return arr
s = Solution()
print s.reaggrange([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])


