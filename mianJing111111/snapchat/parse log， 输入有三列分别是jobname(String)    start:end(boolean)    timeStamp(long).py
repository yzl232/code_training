'''
parse log， 输入有三列分别是jobname(String)    start/end(boolean)    timeStamp(long)， 输入要求是每一个job的start/end time pairs..


其实这个是执行类似round robin以后的步骤，我一开始也没明白。输入可能是这样的：
name(String)    start/end(boolean)    timeStamp(long)
f1                   start                        0
f2                   start                        2.鐣欏璁哄潧-涓€浜�-涓夊垎鍦�
f1                   end                         5
f3                   start                        6
f2                   end                         8
f1                   start                        9. 1point 3acres 璁哄潧
f3                   end                         10
f1                   end                         11. Waral 鍗氬鏈夋洿澶氭枃绔 ,
输出：
f1: [0:5], [9, 11]. 1point3acres.com/bbs
f2: [2, 8]
f3: [6, 10]


啊看了一下，我描述有偏差~应该是：
f1  start  0
// f2  start  2. more info on 1point3acres.com
// f1  start  5
// f1  end   7
// f2  end  10
// f3  start  11
// f3  end   12
// f1  end   15
// f4  start  16
// f4  end   19

// asuming there is only one CPU
// f1: [0,2], [5, 7], [10, 11], [12 15]
// f2: [2,5], [7, 10]
// f3: [11, 12]
// f4: [16, 19. m



这题我也碰到过，在google
后续会问你如何处理recursive call.比如
f1 start 0
f1 start 2
f1 start 4
f1 end 6
f1 end 8
f1 end 10
这时应该只log f1 0 10
当然前提是single cpu single thread


 每个function一个stack, start就push, end就pop, pop完的时候如果stack是空，写入另一个跟你的结构相同的map
'''

#个人思考。  是不是input总valid。 Hash map  f1， f2, f3， 然后2个2个就是valid的