# encoding=utf-8
'''
 第一道题，是说你知道(n&(n-1))得出什么结果吗？



set rightmost 1 to 0




第二题是问我两个 collection 的 object 问 这两个 collection 里面的东西是不是相同的。
我一开始就说把第一个collection object都放到 hashset里面，check 第二里面是不是都包含第一个里面的object
他说怎么处理重复的情况。比如[1,1,2]  [1,2].
我就说换hashmap 记录第一个collection 里面的所有元素的个数，再check 第二个collection.
他要我实现，用伪代码。
码完后问我 时间空间复杂度。后面又问要是不用hashmap 怎么办。我说就把两个都sort了比较。问我复杂度我说o(nlgn). 完了要我问问题，我随便扯了一个。结束。




如何在计算机与计算机之间传送一个二叉搜索树 （传一个先序和一个中序的数组，传过去再恢复树）
 或者serialize。 deserialize




 大数据典型题，只有2g内存，100g的数据，要对100g的数据做排序，说出详细的设计步骤，性能评价在哪，如何优化。
 hash.  成100个文件。  然后分别排序。 归并排序100个文件


 归并的时候，比如2个sorted  10G文件。merge过程 count。 先获得最大的2g文件，存起来。 再继续过程
'''



'''
The third question is a brain teaser: if 1000 couples are to give birth to male and female babies(50% change each), and they would keep giving birth until they have a girl, what's the boy to girl ratio in 20 years

50:50

Yes, that's what makes it a brain teaser, that facepalm moment when you realize no calculation is necessary; each birth is an independent Bernoulli trial and half of all children born will be boys, no matter what each couple's criterion is for stopping.
'''


'''

Table 1: Parents -> (int id, int age)
Table 2: Children -> (int id, int age, int parent_id)
Get the parent id, his/her oldest and youngest children ids.
'''


'''
How to delete two rows from the table in database ?
Note: Delete only first two rows from the Database.

delete from table_name limit 2;
'''