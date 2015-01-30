# encoding=utf-8
'''
大概看一下。 是考察bit运算。 xor




拿着我简历进来，说有人跟你谈过你的简历吗，我说没有，他表示万分惊讶，然后在我
简历上挑了一个research project让我说说，

说完后用c++出了一个题，一个cipher类
，有一个member function是对输入加密，加密方法为对input的每16个Byte和一个
increasing counter做xor，这个increasing counter也是有16Byte，从00..01（前
15Byte都是0，最后1Byte是1）开始，还有一个要求，举例说：
第一个input 有20个Byte，前16个Byte就和00..01做xor，后4个Byte和00..02的前
4Byte做xor
然后之后再对第二个input加密的时候，对这个input的前12Byte用00..02的后12Byte（
即11个Byte 0，1个Byte 1）

然后让我写这个class

我问了一句要是couter的数用完了怎么办，他反问我这个counter有16Byte，多久会用
完。因为已经很累了，算错了好几次，中途我还说16乘以8等于64。。。反正在他逼迫
下我硬着头皮模拟算了一下，得出结果就是很久很久很久才会用完，不用担心。然后又
因为好久没写c或c++，还有真的很累，脑袋一片发麻，茫然不知如何下手，他看不下去
了就说那你就写一个能从小到大生成这个counter能表示的所有integer的函数吧，你要
对python熟一点的话就用Python，这个写完后有两个小bug，迅速改正过来，然后就到
时间了。问我还有没有问题，我就随便问了一下这个office有哪些project，然后就结
束了。
'''