# encoding=utf-8
#n boxes, k balls, expected number of empty boxes.
'''
比如If you have 10 balls and 5 boxes what is the expected number of boxes with no balls.


x = sum(x[i] for i in range(5) )

x[i] = 4**10/5**10

x = 5*   (4**10/5**10)



x = n*((n-1)**k)/(n)**k


'''


'''
 类似的.
  Expected Number with $1$ Ball

x = sum(x[i] for i in range(5) )

x[i] =10*  ( 4**9/  5**10 )

x = 5*  x[i]
 '''
