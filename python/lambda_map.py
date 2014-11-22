# encoding=utf-8
f = lambda x: x*x     #作用。 减少代码行数。 装逼。 适合面试
print f(5)

print map(lambda x:x*x, range(1, 11))
print [x*x for x in range(1, 11)]
'''
注意map, array都比较适合array的操作
'''




'''
map(function, sequence[, sequence, ...]) -> list
通过定义可以看到，这个函数的第一个参数是一个函数，剩下的参数是一个或多个序列，返回值是一个集合。
'''

print map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
#压缩代码行数的利器


print map(f, [1, 2, 3])

def abc(a, b, c): return a*10000 + b*100 + c
list1 = [11,22,33]
list2 = [44,55,66]
list3 = [77,88,99]
print map(abc,list1,list2,list3)


def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)
print F, C




Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)
print Fahrenheit
C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)
print C

'''
filter 在于他是一个函数一个array。而且函数判断依据： 返回boolean, 0, 1, True, False
'''

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result
result = filter(lambda x: x % 2 == 0, fib)
print result

print filter(lambda a:a>0, [-1, -3, 22222, 4])

'''
The function filter(function, list) offers an elegant way to filter out all the elements of a list, for which the function function returns True.
The function filter(f,l) needs a function f as its first argument. f returns a Boolean value, i.e. either True or False.
'''

print reduce(lambda x,y: x+y, [47,11,42,13])




'''
The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value.

If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:

    At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
    In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
    The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
    Continue like this until just one element is left and return this element as the result of reduce()


'''


print reduce(lambda x,y: x+y, [47,11,42,13])

f = lambda a,b: a if (a > b) else b

print reduce(f, [47,11,42,102,13])

#reduce就是不断调用函数。 最后reduce到一个值。返回。