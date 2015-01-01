# encoding=utf-8
'''

第二题是问我两个 collection 的 object 问 这两个 collection 里面的东西是不是相同的。
我一开始就说把第一个collection object都放到 hashset里面，check 第二里面是不是都包含第一个里面的object
他说怎么处理重复的情况。比如[1,1,2]  [1,2].
我就说换hashmap 记录第一个collection 里面的所有元素的个数，再check 第二个collection.
他要我实现，用伪代码。
码完后问我 时间空间复杂度。后面又问要是不用hashmap 怎么办。我说就把两个都sort了比较。问我复杂度我说o(nlgn). 完了要我问问题，我随便扯了一个。结束。
感觉还可以，求onsite。

'''

# 就是简单的sort或者hash.  sort更好。
