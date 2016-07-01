'''
给字符串，写压缩算法，解压算法已有，例如aaabbbbcccc->aaa4xb4xc，需要考虑3aaaaa->35xa会出问题，三哥每次我想了没半分钟就给我提示，最后给的feedback是，需要不停的提示才行。。

压缩字符串, decode function已经给好，让写encode。需要注意的是字符串包含数字和字母，所以类似3ddd不能改写成33xd, 跟面试官交流，被告知不能更改decode function。 所以不能引入特殊字符。

 就是3xd会变成ddd, 11xd会变成ddddddddddd

 请问第一题的encoding是不是碰到数字，不管是几个都要写成几乘几的形式？比如3dddddd就要写成1x36xd？



要encode String以节省空间，有一个固定的decoder，会把3xe 这样的字符串decode成eee，也就是数字乘以（乘号用字母x表示的）字符decode成相应个数的字符。
decoder不能变，写一个encoder，要保证decode会得到原来的字符串。
需要考虑的例子：
                  abc2ddddefg, abc5xefg, abc55555xefg

 encoder, decoder problem. decoder 已经确定不可以更改：作用是 3xa ->  aaa; ab3xcd -> abcccd, 也就是 encoded text -> orginal text；写encoder, 主要是找encoder的special case, orginal text 只有字母和数字，只有字母可以进行缩写：
（1）orginal text 123xa, 如果原样输出则decode结果为 123个a; Solution: encoded as: 123x1xa
  (2) orginal text 3xa, 怎么办： encoded as: 3x1xa
#x变成  x1xa


 解决方法是对于单个数字也encode，如果5变成1x5，上面的例子就不会出产生歧义，缺陷是可能会导致encode后更长。。。
abc2ddddefg 变成 abc1x24xdefg
abc5xefg 变成 abc1x5xefg
abc55555xefg 变成 abc5x5xefg



经典的地里出现过的String压缩编码解码类似题, 后悔当时看到没有好好写过一遍.给一个String比如"abcdfffffffxyz", 写两个methods, encode和decode. encode就是比如"fffffff"变成"7xf",decode就是要变为原字符串.我说"ff"怎么办,他说变成"2xf"你不觉得更长了吗? 我才明白了,应该是encoded后的String要比原来的短,不然为啥要encode,的亏我问了这个问题...然后又问他,如果原String本来就是"5xt"这种结构, decode不就无法辨认了吗?他说很高兴你提出了这个问题,但是不用管它,一会再讨论,先写吧.. more info on 1point3acres.com
写完以后他就问我如果原String本来就是"5xt"这种结构,我encode应该怎么处理? 我就傻了... 因为一直觉得encode后的字符串长度一定要比原来的短,所以根本想不出来他要的解法. 说了四五种方法他都不满意, 最后给我hint说,要是有个"1xt"这样的你怎么处理? 当时脑洞大开想出来了... 其实是要变成三个"1xt"这种结构, 比如原String就是"5xq", 就encode成为"1x51xx1xq"就好了. 但是这种方法违背了encode后要变短的rule,所以我是真没想出来.....
还讨论了好多种情况, 最后一种是"1aaaaa"这种情况怎么变, 我说"1x15xa". 他说这是6个字符,能不能只用5个? 实在想不出来,这时候第三个小哥进来了,韩国哥哥就过来告诉我说,其实看做1a和aaaa两部分encode就好...
面完我就觉得跪了.





老美，从头到尾冷面。只有最后聊他的经历的时候很开心，眉飞色舞。感觉这轮的follow up 有点难。第3）问基本就是他一步一个hint我才答出来的。
    1) encode string： 例如 abbbbbc  -> a5xbc.  我大概花了15分钟写代码。搞定 bugfree。. 1point 3acres 璁哄潧

    2) 如果有个string already in an encoded form, we want to decode it.  Find a type of strings that may cause problem when decoding.
         abbbbbc ->(encode) a5xbc -> (decode) abbbbbc， this one is OK
         a5xbc ->(encode)  a5xbc -> (decode) abbbbbc , this one has problem.   
         实际就是 如果原始string里包含“数字 + x + 任意字符”这种格式的就会有问题。
    3) how to modify the way of encoding/decoding to prevent the problem from happening? . visit 1point3acres.com for more.
         提示：  数字 + x + 任意字符  -> 1x数字1xx
        a5xbc ->(encode) a1x51xxbc -> (decode) a5xbc
-google 1point3acres
       其实第三问我到现在都没搞清楚。请不要问楼主太多关于第三问。。

楼主的的encode那题需要始终对x 和数字编码。例如：
aa51x -> aa1x51x11xx

第二题感谢地里面经，是string encoding，就是aaabbb变3xa3xb那一道题，写了encode的代码，follow u带着一步一步发觉有哪些问题，比如原始string就是3xa怎么办，回答是把数字和x都编码。再问怎么简化一点，答是只用encode数字不用管x。再问如果有重复数字比如2222a呢，答压缩数字4x2a。再问如果有一百万个数字是0123456789012345……的循环，最后跟一个x怎么办，答如果x结尾不用管，不压缩了就。整个过程一半自己想出来一半靠他提示，他其实一直再问，"so what's the general rules?"。。。就是说分情况讨论之前提到的几种情况，保证能够顺利decode。并且不要求每次encode之后string都变短，但是总体上average是变短的。这轮代码写得还行，就是最后general rule答得不好，感觉一般。而且没留时间问问题。。



较麻烦的是怎么保证encode正确，我自己也不确定是不是说得完全对哈：
1. 连续相同字符长度超过3进行压缩
2. 遇到数字（不一定是一位） + ‘x’ + 其他字符的时候，对数字进行压缩。
3. 特殊情况是数字 + 'x'结尾，则不用管。. visit 1point3acres.com for more.

解压缩的时候，直接找每个'x'，如果它之前是数字，它之后有字符，就解压。
'''



