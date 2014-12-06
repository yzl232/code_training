# encoding=utf-8
'''
I have a log that consists of more than 100 million lines. Each line is just a data about user login, login time, etc. I want to sort them based on user login, and then if there is a tie based on login time, etc. However, I have limited memory, so don't think of storing all of them in an array. The memory can only hold n data where n is much smaller than 100 millions. You can access the disk though although it is much slower. How will you do it so that it is as efficient as possible?

这个有点意思。 稍有变化。 全部sort掉。
'''


'''
hash,    mod 1000.  store them to 1000 files.      sort each.
 Then merge sort
'''


'''
We can use external merge sort.
Lets say 100 million entries occupies 900 mb.But we have only 90 mb.
divide 900 mb into chunks of 90mb each and sort them.
2. now pick smallest 10 mb each from these sorted chunks 10 * 9 = 90 and keep remaining 10 mb as buffer.

3. proceed as we do in case of merge sort , When this 10 mb gets filled empty it.
'''