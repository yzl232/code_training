# encoding=utf-8
'''
If you're given a list of countries and its corresponding population, write a function that will return a random country but the higher the population of the country, the more likely it is to be picked at random.
'''

'''
答案非常牛逼。

First of all, sum the population of all countries. Let the sum be N.
Now think of it in terms of a number line. Have a number line from 1 to N. Now allocate proportional part of the number line to corresponding country based on its population (Higher the population more numbers in number line and vice versa). Let say 1 to n1 is for 1st country , n1+1 to n2 to second and so on.
Now generate a random number between 1 to N. Just return the country which owns that number in that number line.
'''


'''
有一列key，每个key有其对应的数值，要求写一个random的函数，key大的返回的概率
也大

把每个key加起来，产生对应的random数，然后按key的大小选key
5,10,20key
产生0到35的随机数
随机数<5,return 5
15>x>=5 return 10
35>x>=15 return 20
'''