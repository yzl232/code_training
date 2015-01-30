# encoding=utf-8


#在mapper和reducer之间， 会自动做好shuffle and sort

#!/usr/bin/env python


# 用到一个pre key

import sys
preKey = None;  total = 0
for line in sys.stdin:
   curKey, val = line.strip().split()
   val = int(val)
   if preKey == curKey:     total += val
   else:
       if preKey:     print preKey, total
       total = val;   preKey = curKey
if preKey:   print preKey, total   ##上上面那行代码一样
# 就是类似count and say




'''
preKey = None
total = 0

for line in sys.stdin:
   line = line.strip()
   curKey, value = line.split("\t")
   value = int(value)

   if preKey == curKey:     total += value
   else:
       if preKey:     print( "%s\t%d" % (preKey, total) )
       total = value
       preKey = curKey

if preKey:   print( "%s\t%d" % (preKey, total) )
'''