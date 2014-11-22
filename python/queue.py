# encoding=utf-8

import collections

d = collections.deque('abcdefg')
print 'Deque:', d
print 'Length:', len(d)
print 'Left end:', d[0]
print 'Right end:', d[-1]

d.remove('c')
print 'remove(c):', d

d.append("x")
print d.popleft()
print d.pop()


e =  collections.deque('abcdefg', maxlen=4)
print e
e.append('y')
print e
e.append('z')
print e

