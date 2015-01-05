# encoding=utf-8
#copy and shuffle lines in a 8 GB file, memory limit 1 GB (you are
#given multiple machines


#line number.    每个line有个line number。 假设有N lines.    然后把这N 个数shuffle。
#如果连只是line number也装不进内存，用比较随机的hash。 然后hash line number ,  %10 。 到10个机器