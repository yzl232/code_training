# encoding=utf-8
'''
How can I represent the following in a data structure ?
<html><body><div><span>TEXT1</span><br/></div></body></html>

Do I do the same using a stack or create a tree for the same ?
'''

# tree
#不能用stack。   比如body下面一层同时有2个div..
#because there could be many tags inside the same tag,  。    linear  data structure做不到。