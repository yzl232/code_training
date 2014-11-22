# encoding=utf-8
'''
Given API:
int Read4096(char* buf);
It reads data from a file and records the position so that the next time when it is called it read the next 4k chars (or the rest of the file, whichever is smaller) from the file.
The return is the number of chars read.

Todo: Use above API to Implement API
"int Read(char* buf, int n)" which reads any number of chars from the file.

一个函数叫int Read4096(char * buf)
每次从stream里面读4Kbytes，如果stream小于4K就读到stream末尾，读出结果放在buf
里面
返回值是读了多少bytes，比如buf长度1Kbytes， 那么返回值就是1024
大于4K的stream连续调用就能自动读到



一个函数叫int Read4096(char * buf)

每次从stream里面读4Kbytes，如果stream小于4K就读到stream末尾，读出结果放在buf
里面
返回值是读了多少bytes，比如buf长度1Kbytes， 那么返回值就是1024
大于4K的stream连续调用就能自动读到底

要求是写一个int ReadBytes(char * buf, num_bytes)
作为Read4096的wrapper，可以在里面直接用Read4096，num_bytes是任意数目，返回值
也是buf的长度，buf就是结果，简单点就是能读任意长度stream的wrapper

挺简单的，结果处理边界和各种判断条件栽了，写了那么久node根本把C++的数组忘干
净了……

'''

class Solution:
    def __init__(self):
        pass

    def read4k(self, readchars):
        pass

#buf 保存读得结果.  没有考虑buffer留下的部分。  可以针对这点问面试官。
    def read(self, buf, n):
        tmpBuffer = [None for i in range(4096)]
        count = 0; tmpN = 4096; flag = True
        while n > count and flag:#tmp的作用就是判断是不是4096。
            tmpN = self.read4k(tmpBuffer)
            if tmpN<4096:  flag=False
            byteN = min(tmpN, n-count)
            buf[count:count+byteN]= tmpBuffer[:byteN]  #结束2个指标 : 1 tmp!=4096.   或者n<=count 完成目标是读n个。或者read4k读完了。
            count+=byteN
        return count

'''
but the read function may be called multiple times.
多次调用的话。tricky多了。 因为之前很可能不满4096的部分，怎么补回来？。。
解法是存为class的相对全局的变量。
'''


class Solution2:
    def __init__(self):
        self.offset = 0
        self.bufsize = 0 #If bufsize > 0, that means there is partial data left in buffer .我们直接复制这里就好。不用call read4k
        self.tmpBuffer = [None for i in range(4096)]
        pass

    def read4k(self, readchars):
        pass

#buf 保存读得结果
    def read(self, buf, n):
        count = 0; tmpN = 4096; flag = True
        while n > count and flag:#tmp的作用就是判断是不是4096。
            if self.bufsize!=0:  tmpN = self.bufsize
            else:
                tmpN = self.read4k(self.tmpBuffer)
                if tmpN<4096: flag = False
            byteN = min(tmpN, n-count)
            buf[count:count+byteN]= self.tmpBuffer[self.offset:self.offset+byteN]  #结束的2个指标 。  1 tmp!=4096.   或者n<=count 读完了。 因为我们目标是读n个。
            self.offset = (self.offset+byteN) % 4096
            self.bufsize = tmpN - byteN  #就是判断有没有残余。   也就是n-count < tmpN吗？
            count+=byteN
        return count

'''
实现 readline，假设提供read4k可以读取4k个字符
'''

class Solution:
    def __init__(self):
        pass

    def read4k(self, readchars):
        pass

#buf 保存读得结果
    def read(self, buf):
        tmpBuffer = [None for i in range(4096)]
        count = 0; tmpN = 4096; flag = True
        while flag:#tmp的作用就是判断是不是4096。
            tmpN = self.read4k(tmpBuffer)
            if tmpN<4096 or '\n' in tmpBuffer: flag = False
            byteN = tmpN
            if '\n' in tmpBuffer:
                byteN = tmpBuffer.index('\n')
            buf[count:count+byteN]= tmpBuffer[:byteN]  #结束2个指标 : 1 tmp!=4096.   或者n<=count 完成目标是读n个。或者read4k读完了。
            count+=byteN
        return count


'''
考了下古，发现这位哥们的转贴，基本可以确认是一个人，基本可以确定这个是我被拒
的原因

同样迟到了大概5分钟，闲扯了十分钟左右，然后read4,确实很简单，但是给的题目非
常不清楚，所以完全没有考虑buffer里面留下的部分，中间我问了除了输出int,需不需
要考虑读出的字符放在哪里，被他含混过去了。自己没做过底层的东西，竟然也没有看
到这个帖子，细节基本一致，因为题目很简单，所以35分钟内完成，全程毫无任何提示
，所有问他的问题基本上都回答得非常模糊，非常有误导性。之后让问fb问题，自己回
答了六周的ramp 什么着，我明明没问。。。最后拍照

我比下面这位哥们唯一好点的地方，我记下了这个人的名字的大致发音,自己查了下
linkedin, 应该是R--it---u---raj Kir---ti

希望以后面fb的诸位，千万小心入口buff需要变动位置，函数外创建类，类里头存上次
buff读入的byte数，然后做移动。

顺便求个bless面l和g的时候别再碰到烙印
===============================================

发信人: will5 (绽放), 信区: JobHunting
标  题: FB临门一脚挂了,那种郁闷悔恨的感觉.
发信站: BBS 未名空间站 (Thu Oct 17 17:55:34 2013, 美东)

上次onsite,4轮,自己感觉很好.
HR回信也说: went well so far but still need last code question interview to
end the process
要安排电话面试
结果我说:电面不好,我要求onsite,今天上午就onsite了.

结果, 一看是一个严肃的老印,基本听不懂其在说什么
就一道题:
实现 int Read(int Size, char * buffer) using int Read4(char * buffer)
这题思路很简单的,我当时给了2种方法结果在他的引导上走上了一条不归路,第一次实
现有bug, 没考虑buffer里面留下的部分....汗 ...各种改...(这题原来有过类似的
readLine, 但是自己觉得应该简单没有动手仔细写过, 结果在press下不能写好, 还是
实力不够!!!)
最后老印拍了照,明显要回去Negative的节奏

也许看到了老印,第一感觉就不妙吧,有了心理暗示, 过程中沟通也不是很顺畅. 面到40
分钟的时候,老印就不出题了, 直接叫问问题.汗

郁闷, 悔恨, 临门一脚, 我是中国足球队吗, 对自己的能力深深的怀疑!!!

再补充几个细节:
1) 此老印说之前在很多公司做过 现在在做Ads这一块. 前面闲扯的时间差不多有78分
钟, 本身他出来接我的时候也迟到了几分钟
2) 在35分钟左右的时候,他就说你问我问题吧, 你就问问我fb的process吧? 我汗, 我
说好的,那你介绍介绍吧, 无非就是6 weeks的ramp up什么的,这些我都知道了,明显是
拖时间到点.
3) 他送我出去的时候,还说:今天只面我一个吗? 我去, 你都送我出来了, 还这样问
4) 全程毫无提示

虽然不能归结为被黑了,但是和之前的 3个老美(或者欧洲) 一个台湾GG 的风格完全不
同, 这四轮过程非常愉快.

也许有人会问, 既然那四轮很好,为什么要加面一轮, 原因在这里:
1. 我没有经过电面,直接onsite的,也许会被认为缺一些coding的考察吧
2.上次四轮, 最后一轮, 第一个问题是: N个平面上点,找离原点最近的K个, 我本来要
给三种方法: 1. N*Log(K) 2.KLog(N) 3.select K 结果说了第一种之后,看他反应不错
,我就问写code吗?他说ok,然后就写完了用priority queue. 当时脑袋蒙了想起select
K的最优解决是 5中取1(不是一般快排的取pivot的方法), 我没信心完全写出code, 就
没说select K的算法.事实上用quicksort写也是很容易的.
至少用priority_queue 写完之后没bug, 后来又写 shift sorted array做binary
search, 写的太快了给人是背答案的感觉,也没bug. 第三个题是实现Heap(其实就是他
对前面的priority_queue有疑问,他说他对priority_queue不熟悉)push pop top, 实现
了最后支出一个小bug,fix


所以我觉得第四轮有一些疑惑再加上没有电面, 加面一轮到是可以理解.

生活没有假设, 也许上次onsite最后一轮直接给最优而不是走了保守策略, 可能也ok了
, 也许这轮onsite像原来希望的交流很smooth(这也是我没有选择telephone interview
的原因)话也会ok的, 也许遇到了困难我能很calm down的去解决问题, 最后结果也可能
不错.
Anyway, 只能move on了, 也祝愿后来的面试的人能多点运气,能一气呵成, 拿到offer!
Bless大家!

'''