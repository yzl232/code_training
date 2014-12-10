# encoding=utf-8
'''
List comprehension is a complete substitute for the lambda function as well as the functions map(), filter() and reduce().

'''


Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print Fahrenheit


#注意这个。  最左边的就是可以代替lambdaL了。  最右边的if就是可以代替filter.  而且filter只有一个array
print [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]


'''
Generator Comprehension
Generator comprehensions were introduced with Python 2.6. They are simply a generator expression with a parenthesis - round brackets - around it. Otherwise, the syntax and the way of working is like list comprehension, but a generator comprehension returns a generator instead of a list.
'''

x = (x **2 for x in range(20))
print x
x = list(x)
print x
print [x **2 for x in range(10)]

'''
圆形括号：  generator
方框括号： array
'''

noprimes = [j for i in range(2, 8) for j in range(i*i, 100, i)] #就是返回2，3， 4， 5， 6， 7的倍数
print noprimes
primes = [x for x in range(2, 100) if x not in noprimes]
print primes

'''
A set comprehension is similiar to a list comprehension, but returns a set and not a list. Syntactically, we use curly brackets instead of square brackets to create a set. Set comprehension is the right functionality to solve our problem from the previous subsection. We are able to create the set of non primes without doublets:
'''

from math import sqrt
