# encoding=utf-8
'''
Write a routine that does secret santa in O(N) time.

A secret santa gift exchange is a game where each player is randomly assigned a person to whom they anonymously give a gift. The algorithm is referred to as Derangement.



The important rules are:

    A person can not be assigned to themselves.
    A person can only be assigned to another person once.
    Assignment must be random.



Secret Santa should mean shuffle the contents of an array where if the index of element represent a person the content would represent the person who is assigned [for gifting] to him.

Input would : 0 , 1, 2, 3, 4 ...n
Output should be : shuffled random contents such that a[i] != i

'''




'''
1) Duplicate the list of people to a second list
2) For every person in first list, select random(size of list) from the second list and remove that person.
Note: make sure not to select identical person. can be done in O(1).
If identical person is selected then add it to the first of the list and then select(random+1)
This will insure that we wont reselect it another time ..

The above solution will take O(n) if find and remove from list is O(1).
This is not the case in linkedlist: find is O(k) itself.
If an array was used as the list then removal is O(n) time (shifting elements after removing)

Keep in mind that we sacrificed space and extra time to build the list in the first place.
'''


#和shuffle那道题基本一样。  range( , 0, ) 就是random(0, i-1)
import  random
class Solution:
    def shuffe2(self, arr):  #O(n) time.  O(n) space
        for i in range(len(arr)-1, 0, -1): #不同
            j = random.randint(0, i-1) #不同。 不能在原地
            arr[j], arr[i] = arr[i], arr[j] #每次保证了不会是自己。 因为自己要么在i后面，要么在原地i。而我们取前i-1
        return arr
s = Solution()
for i in range(5):
    print [0, 1, 2, 3 ,4, 5]
    print s.shuffe2([0, 1, 2, 3 ,4, 5])


# 概率：  last one:   1/(n-1)
#     倒数第二个: n-2/(n-1)  *   1/(n-2)  = 1/(n-1)