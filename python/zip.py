# encoding=utf-8
'''



When you zip() together three lists containing 20 elements each, the result has twenty elements. Each element is a three-tuple.

See for yourself:

In [1]: a = b = c = range(20)

In [2]: zip(a, b, c)
Out[2]:
[(0, 0, 0),
 (1, 1, 1),
 ...
 (17, 17, 17),
 (18, 18, 18),
 (19, 19, 19)]

To find out how many elements each tuple contains, you could examine the length of the first element:

In [3]: result = zip(a, b, c)

In [4]: len(result[0])
Out[4]: 3

Of course, this won't work if the lists were empty to start with.

'''

#作用就是把相同长度的array变成tuple  array