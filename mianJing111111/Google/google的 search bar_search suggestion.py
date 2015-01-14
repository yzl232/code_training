# encoding=utf-8
'''
google的 search bar 里面敲入  一些字母的时候， 会出来一些提示，问
怎么
          实现，我说用 prefix tree.  然后就问， 比如 输入 ca, 出来的可能是
cat,
          california, 问有什么方法可以加快 search, 可不可以提前 search, 我说
可以
           提前 search cat 和 california, 等到用户确定是什么的时候，再输出相
应的
          search的结果， 这样会快一点。


没记错的话这中搜索引擎的auto completion都是用的trie+hashtable+TOP K算法办到的$

每个词用hashtable存频率。
用trie拿出所有符合的prefix,  以及频率， 然后存到heap
'''