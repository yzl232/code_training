# encoding=utf-8
#一个log里有页面的访问记录，如何获得前10popular的（hash_map + heap）
# followup,log里存在多个machine里

'''
 第一重新安排。

   log  hash。 然后mod 分配到各个machine。 这样每个记录key一定在某个machine。

     然后每个都找出top10 、  合并就可以。
     可以用heap或者quick select

'''

#注意一个细节。  得到top10后。  merge一个global的量。  比如top10. 100机器。 merge最多有1000个。  保持这个global的量。
# 然后每个machine取这1000个量的信息。 然后叠加