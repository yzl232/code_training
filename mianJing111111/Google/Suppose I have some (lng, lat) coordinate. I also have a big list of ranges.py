# encoding=utf-8
'''
Suppose I have some (lng, lat) coordinate. I also have a big list of ranges,

[ { northeast: {lng, lat}, southwest: {lng, lat} } ... ]

How can I most efficiently determine which bucket the (lng, lat) point goes into?

Also, on a design perspective. Would it make more sense for the "list of ranges" to be on some database like mysql, monodb, or on something like memcached, redis?
'''

#第二问的答案是yes。  spatial index?
#第一问。不知道啥意思。