# encoding=utf-
'''
is 和 ==的区别。  is比较object.   ==比较值
'''
'''
'''
'''
>>> a = b =3
>>> b=5
>>> a
3
>>> b
5
>>> a = b = [5, 6]
>>> a[0]=1
>>> a
[1, 6]
>>> b
[1, 6]
'''


'''
is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.

>>> a = [1, 2, 3]
>>> b = a
>>> b is a
True
>>> b == a
True
>>> b = a[:]
>>> b is a
False
>>> b == a
True
'''