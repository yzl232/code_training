# encoding=utf-8
'''
Write a function that gets a billion integers. How can you find the midian in most efficient way (time)?

same question, but the input is an endless stream of integers, and we want to find the current median.
'''

#第二个是2个heap
#第一个是
'''
median 海量数据

2).5亿个int找它们的中位数。
　　这个例子比上面那个更明显。首先我们 将int划分为2^16个区域，然后读取数据统计落到各个区域里的数的个数，之后我们根据统计结果就可以判断中位数落到那个区域，同时知道这个区域中的第 几大数刚好是中位数。然后第二次扫描我们只统计落在这个区域中的那些数就可以了。

　 　实际上，如果不是int是int64，我们可以经过3次这样的划分即可降低到可以接受的程度。即可以先将int64分成2^24个区域，然后确定区域的 第几大数，在将该区域分成2^20个子区域，然后确定是子区域的第几大数，然后子区域里的数的个数只有2^20，就可以直接利用direct addr table进行统计了。







方法同基数排序有些像，开一个大小为65536的Int数组，第一遍读取，统计Int32的高16位的情况，也就是0-65535，都算作0,65536 - 131071都算作1。就相当于用该数除以65536。Int32 除以 65536的结果不会超过65536种情况，因此开一个长度为65536的数组计数就可以。每读取一个数，数组中对应的计数+1，考虑有负数的情况，需要 将结果加32768后，记录在相应的数组内。

第一个pass, 统计各个区间的数目。

比如1~1000， 有800个数。  1001~2000 有600个数。 然后可以知道在哪个区间。

第一遍统计之后，遍历数组，逐个累加统计看中位数处于哪个区间，比如处于区间k，那么0- k-1的区间里数字的数量sum应该<n/2（2.5亿）。而k+1 - 65535的计数和也<n/2

第 二遍统计同上面的方法类似，但这次只统计处于区间k的情况，也就是说(x / 65536) + 32768 = k。统计只统计低16位的情况。并且利用刚才统计的sum，比如sum = 2.49亿，那么现在就是要在低16位里面找100万个数(2.5亿-2.49亿)。这次计数之后，再统计一下，看中位数所处的区间，最后将高位和低位组 合一下就是结果了。







案1：先大体估计一下这些数的范围，比如这里假设这些数都是32位无符号整数（共有2^32个）。我们把0到2^32-1的整数划分为N个范围段， 每个段包含（2^32）/N个整数。比如，第一个段位0到2^32/N-1，第二段为（2^32）/N到（2^32）/N-1，…，第N个段为 （2^32）（N-1）/N到2^32-1。然后，扫描每个机器上的N个数，把属于第一个区段的数放到第一个机器上，属于第二个区段的数放到第二个机器 上，…，属于第N个区段的数放到第N个机器上。注意这个过程每个机器上存储的数应该是O(N)的。下面我们依次统计每个机器上数的个数，一次累加，直到找 到第k个机器，在该机器上累加的数大于或等于（N^2）/2，而在第k-1个机器上的累加数小于（N^2）/2，并把这个数记为x。那么我们要找的中位数 在第k个机器中，排在第（N^2）/2-x位。然后我们对第k个机器的数排序，并找出第（N^2）/2-x个数，即为所求的中位数的复杂度是O（N^2） 的。

    方案2：先对每台机器上的数进行排序。排好序后，我们采用归并排序的思想，将这N个机器上的数归并起来得到最终的排序。找到第（N^2）/2个便是所求。复杂度是O（N^2*lgN^2）的。









Given a list of 4 billion integers, find an integer not in the list using 4MB of memory. (interview was in Java)







         It’s possible to find a missing integer with just two passes of the data set. We can divide up the integers into blocks of some size (we’ll discuss how to decide on a size later). Let’s just as- sume that we divide up the integers into blocks of 1000. So, block 0 represents the numbers 0 through 999, block 1 represents blocks 1000 - 1999, etc. Since the range of ints is finite, we know that the number of blocks needed is finite.

         In the first pass, we count how many ints are in each block. That is, if we see 552, we know that that is in block 0, we increment counter[0]. If we see 1425, we know that that is in block 1, so we increment counter[1].

         At the end of the first pass, we’ll be able to quickly spot a block that is missing a number. If our block size is 1000, then any block which has fewer than 1000 numbers must be missing a number. Pick any one of those blocks.

         In the second pass, we’ll actually look for which number is missing. We can do this by creat- ing a simple bit vector of size 1000. We iterate through the file, and for each number that should be in our block, we set the appropriate bit in the bit vector. By the end, we’ll know which number (or numbers) is missing.

         Now we just have to decide what the block size is.

         A quick answer is 2^20 values per block. We will need an array with 2^12 block counters and a bit vector in 2^17 bytes. Both of these can comfortably fit in 10*2^20 bytes.

         What’s the smallest footprint? When the array of block counters occupies the same memory as the bit vector.
'''