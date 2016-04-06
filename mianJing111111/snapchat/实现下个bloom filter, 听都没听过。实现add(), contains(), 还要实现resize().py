'''
1. bloomfilter, follow up  如何support remove element from bloomfilter, 当insert element很多以后, 如何扩充容量


 准备的题目一道也没用上，搜了下才知道是onsite题，让实现下个bloom filter, 听都没听过。实现 add(), contains(), 还要实现resize()。
 
 
 bloomfilter， 支持add， mightcontains，resize，remove.
 
 
bloomfilter 是一种数据结构。用到了hashmap和Bit array.
'''


# http://glowingpython.blogspot.com/2013/01/bloom-filter.html

'''
我面的题目是实现一个bloomfilter
        设计一个hash函数，根据传入的整数值不同，产生不同hash结果，
        同一个对象，通过不同的函数映射到多个位置，将这些位置保存为1
        删除，可在每位上使用计数器



如果remove的操作并不会有很多的话  可以专门开个hashset之类的东西存已经被remove的element.....   我还以为是很高大上的解法  然而并没有

如果remove的操作并不会有很多的话  可以专门开个hashset之类的东西存已经被remove的element.....   我还以为是很高大上的解法  然而并没有



if you want to resize a bloom filter secondary storage of keys is required.
很蠢的芳发把keys都存起来..

'''

class BloomFilter:
    
    def __init__(self, size, hashes):
        self.size = size
        self.hashes= hashes
        self.bit_array = [0] * (size)   # array of bits (0, or 1)
        
    def add(self, s):
        for h in self.hashes:
            self.bit_array[h.hash(s) % self.size] = 1    # %size防止index out
            
    def contains(self, string):
        return all(self.bit_array[h.hash(string) % self.size] for h in self.hashes)
        
        
'''
        
size 逐渐增大比较好，可以控制 false positive rate。
. from: 1point3acres.com/bbs
比如按 power of 2 增长。


加上删除
class BloomFilter:

    def __init__(self, size, hashes):
        self.size = size
        self.hashes= hashes
        self.bit_array = [0] * (size)   # array of bits (0, or 1)
        self.count = [0]*(size)

    def add(self, s):
        for h in self.hashes
            t = h.hash(s) % self.size
            self.bit_array[t] = 1    # %size防止index out
            self.count[t] += 1

    def contains(self, string):
        return all(self.bit_array[h.hash(string) % self.size] for h in self.hashes)

    def remove(self, string):
        for h in in self.hashed:
            t = h.hash(string) % self.size
            if self.bit_array[t] == 1:
                self.count[t] -= 1
                if self.count[t] == 0:
                    self.bit_array[t] = 0





class BloomFilter:
    
    def __init__(self, size, hash_count):   
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * (size)   # array of bits (0, or 1)
        
    def add(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size   # %size防止index out 
            self.bit_array[result] = 1
            
    def contains(self, string):
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return False
        return True
        
   
'''