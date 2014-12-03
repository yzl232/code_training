# encoding=utf-8
'''
there are N nuts and N bolts, all unique pairs of Nuts and Bolts. You cant compare Nut with Nut and a Bolt with Bolt. Now ,how would you figure out matching pairs of nut and bolt from the given N Nuts and Bolts.

'''


'''
方法就是类似快排，随便找一个螺母a，用它把所有螺栓分成小于a、大于a和等于a（只有一个）。再用那个等于a的螺栓把所有螺母也划分一遍。于是就得到了一对匹配和“大于a的螺母螺栓”、“小于a的螺母螺栓”两部分，递归处理。复杂度和随机选取pivot的快排的复杂度一样。
'''

#code很难写。 懒得写了。

