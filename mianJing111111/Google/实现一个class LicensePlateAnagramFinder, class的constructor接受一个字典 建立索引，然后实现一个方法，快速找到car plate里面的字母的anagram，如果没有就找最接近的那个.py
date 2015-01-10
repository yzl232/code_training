# encoding=utf-8
'''
实现一个class LicensePlateAnagramFinder, class的constructor接受一个字典 建立索引，然后实现一个方法，快速找到car plate里面的字母的anagram，如果没有就找最接近的那个
'''

'''
直接对字典里的所有词做个trie， 然后对于plate里字母的所有anagram进行查询。因为短，所以anagram数目不多。预处理做的多一些但是查询快吧，
'''


#另外就是和之前相同。 hashtable  赤裸裸暴力。
#和这道题一样。

#优化。 车牌号很短。 字母更短。  所以字典里长单词可以舍去。
#trie没有优化多少。