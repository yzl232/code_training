# encoding=utf-8


#在mapper和reducer之间， 会自动做好shuffle and sort

#!/usr/bin/env python



#代码都几乎一样
import sys

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