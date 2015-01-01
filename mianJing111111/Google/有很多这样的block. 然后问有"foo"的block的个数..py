# encoding=utf-8
'''
第一题是, 给一个很大文件, 格式是这样的:

{
    foo=1
    bar=2
    baz=13
    ...
    ...
}

有很多这样的block. 然后问有"foo"的block的个数.
'''

class Solution:
    def cnt(self, f):
        contents = f.read().split("}")
        cnt = 0
        for block in contents:
            i = block.index('{')
            if 'foo' in block[i:]: cnt+=1
        return cnt

#因为确认了格式正确 所以这样做可以