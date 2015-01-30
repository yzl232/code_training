# encoding=utf-8
'''
8
感觉就是考网络，地球和月球服务器之间发，月球服务器之间。我也没啥思路，

就提到
月球和地球之间通讯越少越好，用checksum检查数据是否正确。还得分包，因为一个
package可能不够装kernal要该的内容。

这题有很多点可以挖掘，比如kernal文件是发
所有的文件还是类似于svn的那种。100台服务器之间怎么传递要修改的kernal信息，需
不需要等到所有kernal信息都收到了才开始发。整个protocol怎么设计，每个package
需要什么header。
'''

#我自己感觉类似sync。  用split成较小的部分。  checksum    to 。  只要同步较小的部分就好了。
# 另外以树的形状来传
#        r0
#   r1       r2
#r3  r4    r5 r6

