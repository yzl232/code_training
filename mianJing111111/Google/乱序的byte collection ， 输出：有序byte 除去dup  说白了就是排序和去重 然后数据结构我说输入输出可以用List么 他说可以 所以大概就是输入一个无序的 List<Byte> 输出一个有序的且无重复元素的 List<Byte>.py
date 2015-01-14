# encoding=utf-8
# 乱序的byte collection ， 输出：有序byte 除去dup  说白了就是排序和去重 然后数据结构我说输入输出可以用List么 他说可以 所以大概就是输入一个无序的 List<Byte> 输出一个有序的且无重复元素的 List<Byte>

#作为byte。 一共是256个可能值
# bool[256] 就可以了

#它要求无重复。