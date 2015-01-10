# encoding=utf-8
'''
假设有一个显示一个公司实时估价的网站，不断的会有最新价格进来（每个价格都会贴上一个timestamp，用于标识），要求提供几个方法查询highest price,和latest price。问如何实现。。。同时该系统支持add(timestamp, price)，和update(timestamp, price)。add()即添加新价格，update即根据timestamp来跟新以前的数据。
- 系统不用提供删除操作
- 假设add()进来的price的timestamp都是递增的，即timestamp没有重复。

- follow up，如果add()需求很大，update只是偶尔的操作，该怎么解决。
解答
我用的是max heap+hash来解决highest pric，用一个变量来解决latest price(因为不要求删除)。
follow up
之前的add()和update()操作都是O(logN)，follow up之后，不再维护heap，将add()降低为O(1)的操作，update()变为O(N)的操作。
'''


#第一个： heap+hashtable.  还有一个单元变量 latest.
#再加上那个一个hashtable。  可以查询O(1).   hashtable里边存了pointer to heap
#add()和update()操作都是O(logN)


# follow up:   单元变量   maxVal,  latest Val .   Hashtable 用来更新  都是O(1)