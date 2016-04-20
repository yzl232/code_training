# encoding=utf-8
'''
+1 North America
...
+1950 Northern Cal
…
+44 UK
+4420 London
+447 UK Mobile
+44750 Vodafoned
…

and we have a phone number, for instance
+447507439854795
+44989045454

return where the number is from

'''
#G家经典。 的trie。  找prefix   .     prefix所在的就是match了。

# trie的 _end key存地址的值。

'''
使用trie的基本思想是没有错的.
self.ret.   搜索.  每次找到一个end. 更新self.ret.
'''