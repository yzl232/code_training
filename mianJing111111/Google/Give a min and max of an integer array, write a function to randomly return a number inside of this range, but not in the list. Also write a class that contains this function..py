# encoding=utf-8
'''
Give a min and max of an integer array, write a function to randomly return a number inside of this range, but not in the list. Also write a class that contains this function.
'''
#和 这道题目像
#与之前的区别在于加了一个minV, 变成 jump+x+minV

#背下。不大理解
import random
class Solution:
    def randK(self, arr, minV, maxV):
        arr.sort();  n=maxV-minV+1-len(arr)
        x = random.randint(0, n-1)
        x = minV+x  #多了这一步而已
        for y in arr:
            if y>x: return x
            x+=1
        return x
#极端情况0, 1, 2 ,3
 #   def cntLessOrEqual(self, ):

s = Solution()
for i in range(3):
    print s.randK([1, 2, 4], 1, 6)


'''
We can have this algoirthm:
1. Sort the given list. It takes time O(nlogn)
2. Instead of creating an array we can just get the size of the array, i.e., number of elements which are not present in the given list. It will be
size = (max-min+1) - (number of distinct numbers in the list)

3. Now we can get a random number k in the range [1,size]

4. Now we just need to find the kth number among the numbers which are not present in the given list. We have not created the array of missing numbers. So we will find the kth number among the missing numbers using the given list as follows:
a) take curr = min
b) take num = curr + k - 1 (taking k to bestarting from 1)
c) do binary search to find element in the list which is the rightmost element less than or equal to num. Label it as lower_element
基本上就是binary search之后的h了。 l是后面的一个

If no such element exists, then num is less than first element in the list, so num is the answer.
Otherwise,
(i) count the number of elements from lower_element in this traversal to the lower_element in previous traversal (if first traversal, count number of elements from starting)
(ii) k = (count in step (i))
(iii) num = num + k


Example:

List is {10, 20, 40, 60, 80} //taking sorted list for convenience.
Range is 1-100

Step 2.
size = (100-1+1) - 5
= 95

Step 3.
Random number generated = 50

Step 4.

a) curr = 1
b) num = 1+50-1 = 50
c)
First traversal:
search for 50 in the given array.
lower_element = 40
i) count = 3
ii) k = 3
iii) num = 50+3 = 53

Second traversal:
search for 53 in the given array after 40.
There is no lower_element now.

So the answer is 53.

Basic Assumption: We have a function that generates a pure random number from 1 to n.
'''



# encoding=utf-8
'''
Implement below function.
int getRandom(int N, int K[])

Constraints:
->K is sorted and contains elements in range [0,N)
->Output should be a random number between [0,N) excuding elements from K
->probability of generated number should be 1/(N-K.length) and not 1/N
-->int uniform(int N) is given which returns random number [0,N) with 1/N probability for each number.
->No more than O(1) memory
->No more than O(N) time
'''
