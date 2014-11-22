# encoding=utf-8
'''
A company has decided to increase salary of all the employees. These employees are divided into 3 categaries: A B C. The people in C category gets N percentage increase.The people in B category gets 2*N percentage increase.The people in A category gets 3*N percentage increase. The minimum increase should be atleast 1% and no matter what the percent be the maximum increase should not increase $75000. Write a function which takes appropriate input and calculates the increase and updated salary. Print the increase for the employee and the return the updated salary.
'''

class Solution:
    def rmoney(self, base, case, n):
        increase = 0.01
        if case=='A': increase = n*0.01
        elif case=='B': increase = n*0.02
        else: increase = n*0.03
        increase = max(0.01, increase)
        if base>=75000:
            print 0
            return base
        if base*(1+increase)>75000:
            print  75000-base
            return 75000
        else:
            print base*increase
            return base*(1+increase)