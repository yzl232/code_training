# encoding=utf-8
#一个log里有页面的访问记录，如何获得前1000popular的（hash_map + heap）
# followup,log里存在多个machine里

'''
 第一重新安排。

   log  hash。 然后mod 分配到各个machine。 这样每个记录key一定在某个machine。

     然后每个都找出top1000 、  合并就可以。
     可以用heap或者quick select

'''