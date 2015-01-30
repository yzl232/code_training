# encoding=utf-8
#只是简单地打印出key, val而已。
#!/usr/bin/env python

import sys
for line in sys.stdin:
   keys = line.strip().split()
   for key in keys:   print key, 1


# map 和 reduce都是以 最为基本的line,  line.split() 为操作标准的

'''
for line in sys.stdin:
   keys = line.strip().split()
   for key in keys:
       value = 1
       print( "%s\t%d" % (key, value) )
'''