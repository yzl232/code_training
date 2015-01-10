# encoding=utf-8
#Design a Crossroad signal system


#关于面向对象。 每个物品， 都作为一个class
#  class Road,  car, light, direction.

'''
while True:
    color = red
    time.sleep(60)
    color = green
    time.sleep(30)
    color =
'''

#

'''
public class TrafficLight {
    public static final int RED = 0;
    public static final int YELLOW = 1;
    public static final int GREEN = 2;
    private int currentColor = RED;
    public int change() {
        switch (currentColor) {
        case RED:
            currentColor = GREEN;
            break;
        case YELLOW:
            currentColor = RED;
            break;
        case GREEN:
            currentColor = YELLOW;
            break;
        }
        return currentColor;
    }
    public int getCurrentColor() {
        return currentColor;
    }
}
'''
'''
'''







'''
Here is my take:
A simple crossroad can have traffic moving in 8 possible combinations:
1. Curve paths: East->North, North->West, West->South and South->East (first is the inital direction of motion and second is the direction after making a curve).
2. Straight path: All four directions.

Out of this two can happen at the same time:
ex: North->West and South->East and also in heading east and heading west can flow at the same time.

Thus out of eight combinations we have to decide only among 4 combinations, this is similar to a 2 bit problem where the state can revolve around four possible states:
00
01
10
11

'''
