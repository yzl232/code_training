# encoding=utf-8
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
            small = min(i for i in a if i[1]==0)       #0里边找个子最矮的
            result.append(small[2])  #站在队伍前面的潜在cadidates.     tallNum
            a.remove(small)
            for i in range(len(a)):
                if a[i][0]<small[0]:  a[i]=(a[i][0], a[i][1]-1, a[i][2])  #如果比small矮，则要更新一下tallnum了，减一
        return result

s = Solution()
print s.printQueue( [(6, 2, 'a'),(1, 4, 'B'),(11, 0 ,"C"),(5, 1, 'D'), (10, 0, 'E'),(4, 0, 'F')])