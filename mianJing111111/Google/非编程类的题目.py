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
 或者serialize。 deserialize.
 我感觉serialize更好一点。




 大数据典型题，只有2g内存，100g的数据，要对100g的数据做排序，说出详细的设计步骤，性能评价在哪，如何优化。
 hash.  成100个文件。  然后分别排序。 归并排序100个文件


 归并的时候，用heap
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



'''
What would happen if you have only one server for a web cache (a web browser cache whose key is url and value is the loaded content of the webpage) but huge numbers of clients? And how would you solve it? Assume the cache is implemented with a hashmap and a linkedlist.

可能的答案。
Lot of clients and only one server implies that the data in the cache will be flushed out soon as you cannot store data of all the urls data in cache. So, cache will not help in reducing the response time

The question looks a little incomplete in terms of the problem statement. Hashmap and linkedlist seems to me LRU cache implementation. The items (keys) of the hashmap point to the nodes in linked list and the payload of linked list has the value (page content cache). After every fetch operation the head points to the element just fetched. That way the last element is always the least recently used and would be thrown off the cache when the cache is full with n keys. This way the caching server would work optimally by having a high cache hit for frequently used pages and a cache miss would occur more frequently for infrequently visited pages.

'''



'''
onsider a scenario where you open a file with your favorite editor (emacs on Linux or Microsoft Word on Windows).
You notice that the application has a performance hit due to a recent fix made to the Editor application.
What will your testing Matrix look like that will convey the information that the performance of the application has degraded (or improved after bug fixes and re-design)?

In other words, the interviewer was saying that, if we had a graph showing values obtained from tests run over time for:

File I/O, hardware configuration, software configuration, graphics system, GPU, CPU etc.

then at the End Of the Day, looking at the reports, which parameters will instantly tell you that the performance has definitely increased?
(Also in other words he was asking the Matrix that will portray those parameters).
'''




'''
If you have data coming in rapid succession what is the best way of dealing with redundant data?


The question is probably intentionally vague. Here we don't have access to the interviewer here to ask questions so we should make our own assumptions. If the range of the incoming data is small then we can fit all the hash table in memory and the solution is pretty trivial. But if the range is very big (like finding duplicate incoming images in imgur), we need a huge hash table to minimize collisions and we need to also think about how to map the data to a hash key. In this case the hash table might no longer fit in the memory or even in the same machine. Another important question to ask if duplicates happen often or rarely. If the answer is rarely then we can use bloom filters to check very quickly whether the incoming data is not present in our database (bloom filters are 100% accurate when they determine a data is not present in the set, otherwise we have to go to database to check for the answer).
'''


'''
How does trie handle scalability as opposed to hashtable? Assuming it is used for a dictionary. Sclability here should cover large size of input, running out of memory, or even running out of memory on multiple machines if distributed system is used.


You can easily distribute hash table into hundreds/thousands machines by assigning each machine a key range. Each machine will know what other machine is responsible for the give key. So any key can be looked up with at most two machine forwards.

you can have like aa to machine 1, ab to machine 2 and so on. That gives you 26*26 machines and each can know abt the other just like hashmaps. (Ofcourse, the special case of the word 'a' etc that can be stored specifically in say the first machine aa)


With trie distribution of words across m/cs will be non-uniform if you split by prefixes.

For hashtables, the quality of your hash function determines the distribution of data.

'''





'''
if EVER + SINCE = DARWIN , then what is D+A+R+W+I+N?


dont know how

But got it with google

1. As it's a sum of 3 numbers hence the maximum value of D could be 2 or 1, but then we look at S which could have maximum value 9 and if it gets a carry of 1 then the value of A will be 0 and the D=1.
2. Then we looks at E and I which results in R, as 9 is already occupied by S so E could be 8 and I could be 7 and R will be 5 with carry 1.
3. Then we place the values of R=5 and E=8 resulting in N=3 with carry 1.
4. In ten's digits - E=8 and and value of C could be 3,4,6 (As all others are occupied) and To make I=7 (previously assigned in step 2) E must be added by 9 which is already occupied by S. So this hit ends here.
Now start again with reduced value of E or I, repeat above steps until you get a correct answer or a dead end.
5. Repeating above steps one time comes with E=5 and I=7 which results in R=3 carry=1.
6. Placing R=3 and E=5 in unit digits and their sum gives 8.
7. in ten's digits place E=5 now you can add 2 to make I=7 hence C=2.
8. in 100's digits you have N=8 (from step 6) and only digits that are left now are 4 and
6 hence. So placing V=4 you will get W=2 which is not true because it is already assigned to C. So we are left with only V=6 as the ultimate choice and this leads the result in to W=4.

Hence this way we got the answer

....5 6 5 3
....E V E R
..9 7 8 2 5
+ S I N C E
----------------------
D A R W I N
1 0 3 4 7 8

Hence D+A+R+W+I+N = 1+0+3+4+7+8 =23

'''



'''
3. search BST的worst case， 原因
    答： O(n), BST不balanced
4. 怎么改善
    答： reconstruct BFS。
我问小哥，你会怎么做？
答： 你的方法可以，或者AVL tree。

'''