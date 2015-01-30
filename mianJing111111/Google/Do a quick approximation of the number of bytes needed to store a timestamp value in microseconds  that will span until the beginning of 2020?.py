# encoding=utf-8
'''
Do a quick approximation of the number of bytes needed to store a timestamp value in microseconds

that will span until the beginning of 2020?

Quick approximation: --> come up with an answer without doing complicated operations (i.e. no

calculator, just back of the envelope computations).

1s = 1000*1000ms   # 微秒,也就是百万分之一秒.

1min = 60s

1h = 60 m

1d 24 h

1y = 365d


6年

一共多少个。 timestamp = 6* 365*24*60*60*1000*1000

10^14

2^3.3

2^(14*3.3)=2^47
2

一共是42个bit。  那就是6个byte

47/8 =~ 6

6bytes

'''