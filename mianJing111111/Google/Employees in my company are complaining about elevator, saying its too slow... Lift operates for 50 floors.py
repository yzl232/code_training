# encoding=utf-8
'''
Employees in my company are complaining about elevator, saying its too slow... Lift operates for 50 floors

I hire you and you have to tell me what is the problem and solutions to it.

Input:
Motor can't be changed
You can't get a new elevator as its too costly.

Get 5 matrices you would collect and how would you use them.
'''

#设计elevator    youtube有视频。。。
# who will use the elevators?  children, adults, old people.? disabled?
# 状态 up, down,  loading, idle, on,   beep,...   可以是一个finite state machine
# max flow.   average flow.
#  多少层。  决定多少elevator
# speed
# passenger  exit, enter time
#  max_passenger
#  https://www.youtube.com/watch?v=fITuhLSwbt8

'''
class Elevator,
    id   .
   direction, state.    passengers. capacity . speed.

class Passenger:
        name, age.  destination.


class Floor:
       number,


private elevator,  staff elevator,  passenger elevator ,

'''




'''
Matrices gathered can be:
1> Average number of employes using the lift during the peak times(morning time and evening time)    高峰人数
2> Age distribution of the employes using the lift at peak times      年龄分布。
3> Average number of times the lift changes direction(moving up to moving down, moving down to moving up)
多少次改变方向
4>Floors where the crowd is more  . 哪层人更多。
5>Lift door open and closing time.   开合需要的时间。

By knowing the average number of people using lift at peak times, may be its worth suggesting to management to get another lift.

With age distribution, we can suggest young employees to use stairs if possible.

The number of times the lift changes the direction, may be useful in improving the algorithm used by the lift for servicing requests.

For crowded floors, may be there can be separate lift movements at specific times of the day serving these floors.


Reduction in the door opening and closing timing may have some improvement.
'''