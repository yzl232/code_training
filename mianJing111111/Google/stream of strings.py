# encoding=utf-8
'''
stream of strings like this
"1 34 5 6"
"3 4 5 6 3"
"4 5 6 3 3"
...
每行是一个包含数字的string。去除所有数字完全重复的strings.比如这里的第二和第三行数字完全相同，可以合并成一个。要求合并所有数字完全重复的strings。
 这两个不能合并，因为里面元素不完全相同。必须元素以及个数都一样才能合并。




 stream of strings like this
"1 3 4 5 6"
"3 4 5 6 3"
"4 5 6 3 3"
...

这个是anagram的变体，用anagram的解法即可。

换言之只需要统计每个字符串里，每个字符出现的次数.这里字符仅限0-9，因此可以建
立一个表int[] statics = new int[10]; 然后保持0-9出现的次数。对每个字符串计算
一次，然后用hashSet来保持这些statics.遇到重复值，即为每个数字完全一样的，可
以遗弃。

如果不是数字，而是unicode字符，那么以上解法无效。必须对字符串按字符排序放进
hashSet。

如果是unicode字符串，每个字符串又很长。。。。大概要变成设计题，套轮子了。
'''



#就是类似anagrams。  排序string后，查hashMap里面有没有存。  有的话，就无视之