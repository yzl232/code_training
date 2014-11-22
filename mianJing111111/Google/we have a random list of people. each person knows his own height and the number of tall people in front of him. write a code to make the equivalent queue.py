# encoding=utf-8
import random
'''
we have a random list of people. each person knows his own height and the number of tall people in front of him. write a code to make the equivalent queue.
for example :
input: <"Height","NumberOfTall","Name">,
<6,2,"A">,<1,4,"B">,<11,0,"C">,<5,1,"D">,<10,0,"E">,<4,0,"F">
output: "F","E","D","C","B","A" --> end of queue


想法非常赞
dequeue(set of people)
	filter all people who have 0 no of people in front of them
		//as 0 means either they are in the front of the queue or all people ahead of them are smaller than them
	find the person with smallest height
		//this will be the guy standing at the front of the queue
	As this person will be removed so all people having height less than him and behind him (no of tall > 0) will no longer be able to see him. So we need to reduce the count of no of tall people by 1 for each
	print the person and call the function with the remaining set of people.


 [(6, 2, 'a'),(1, 4, 'B'),(11, 0 ,"c"),(5, 1, 'D'), (10, 0, 'E'),(4, 0, 'F')]


 O(n2)
'''


class Solution:
    def printQueue(self, a):
        result = []
        while a:
            tmp = []
            for i in a:
                if i[1] ==0: tmp.append(i)    #站在队伍前面的潜在cadidates.     tallNum
            small = min(tmp)        #个子最矮的
            result.append(small[2])
            a.remove(small)
            for i in range(len(a)):
                if a[i][0]<small[0]:   #如果比small矮，则要更新一下tallnum了，减一
                    a[i]=(a[i][0], a[i][1]-1, a[i][2])
        return result

s = Solution()
print s.printQueue( [(6, 2, 'a'),(1, 4, 'B'),(11, 0 ,"c"),(5, 1, 'D'), (10, 0, 'E'),(4, 0, 'F')])


#解法2.  注意。下面是错的。。  证明了我的解法是错的。哈哈.


class Person:
    def __init__(self, height, frontTallNum, name):
        self.name = name
        self.height = height
        self.frontTallNum =frontTallNum

def myCMP(one, other):
    if one.frontTallNum == other.frontTallNum and one.height==other.height: return 0
    elif one.frontTallNum != other.frontTallNum: return 1 if one.frontTallNum>other.frontTallNum else -1
    return 1 if one.height>other.height else -1


arr =  [(6, 2, 'a'),(1, 4, 'B'),(11, 0 ,"c"),(5, 1, 'D'),(4, 0, 'F'), (10, 0, 'E')]
persons = []
for t in arr:
    p = Person(t[0], t[1], t[2])
    persons.append(p)

print persons[0]>persons[1]

persons.sort(myCMP)
for p in persons:
    print p.name
