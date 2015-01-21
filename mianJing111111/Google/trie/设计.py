# encoding=utf-8
'''

为一个城市人口设计电话簿的数据结构。
要求就是：
如果输入phone num，比如输入800-111-XXXX， 就要把所有的 电话号码以800-111开头
的name都找出来

另外如果输入name，比如输入john，则要返回所有的first name等于john的电话号码。

我知道的办法就是建立2个trie：为phone num建立一个trie，为name再建立一个trie




Google和百度那种搜索关键字输入的框框，你输入一半字符串它会在下拉列表里按搜索频率高低显示关键词。比如你输入"hel",下拉框显示"hello","hell","hellokitty", "hellokitty



trie tree可以方便的找到所有特定字符串开头的搜索项。
找到所有的匹配字符串
然后用O(n)的复杂度找出这些搜索项中最频繁的k个搜索.   或者sort    nlogN
minheap    = k
N logK



俺面试S家的时候，让写一个suggestion system，俺写出了trie的几个function，结果
挂了。




Which data structure will you use for creating a real world dictionary?

Trie.
 Fast searching , dictionary like indexing.
'''
