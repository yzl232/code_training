# encoding=utf-8
'''
实现一个class LicensePlateAnagramFinder, class的constructor接受一个字典 建立索引，然后实现一个方法，快速找到car plate里面的字母的anagram，如果没有就找最短的那个
'''
#居然出现了三次


'''
直接对字典里的所有词做个trie， 然后对于plate里字母的所有anagram进行查询。因为短，所以anagram数目不多。预处理做的多一些但是查询快吧，
'''


#另外就是和之前相同。 hashtable  赤裸裸暴力。
#和这道题一样。

#优化。 车牌号很短。 字母更短。  所以字典里长单词可以舍去。
#trie没有优化多少。

'''
Problem
Given a dictionary of words and the characters from a license plate, find the shortest word in the dictionary that contains every letter found in the license plate.
Example:
License plate:        ABC1234
Dictionary:        { “cab”, “cat”, “back”, “abacus”, “syzygy” }
Solution:        “cab”

最快O(length of dictionary * length of string),用hashmap做的,做完后让做了一些细节优化,比如如果word的length比res的length长,就skip这个word,然后又优化先把Dictionary
sort(这里写了一个comparator,因为要根据length sort,然后如果在短的word中找到了,就直接输出)
follow up是输出，所有最小长度的word,做法差不多
License: abc1324
Dictionary:        { “cab”, “cba”, “back”, “abacus”, “syzygy” }0 w8 R: J2 l  N" o1 ?" A% V5 v: `
Solution:        “cab” “cba”
'''



'''
給一個車牌號碼(美國的)，以及一個dictionary，請找出dictionary裡含有所有該車牌號碼裡的所有英文字母(case insensitive)的最短字串。
ex:
車牌 RO 1287 ["rolling", "real", "WhaT", "rOad"] => "rOad"

follow up:
(1) 如果dictionary裡有上百萬個字，該如何加速?
(2) 如果dictionary有上百萬個字，然後給你上千個車牌號碼，要你回傳相對應的最短字串，該如何optimize?
'''

# 对应的一个arr[62].   preprocesss保存。 对应的最短的字串。。  然后如果车牌号对应的cnt array相同。 就不用重复找了。
# 比如如果word的length比res的length长,就skip这个word,

'''
最快O(length of dictionary * length of string),用hashmap做的,做完后让做了一些细节优化,比如如果word的length比res的length长,就skip这个word,然后又优化先把Dictionary
sort(这里写了一个comparator,因为要根据length sort,然后如果在短的word中找到了,就直接输出)
'''