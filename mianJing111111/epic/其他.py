# encoding=utf-8
'''
35 cents is paid by two coins one is not a dime. What are the two coins?


Quarter and dime. This is more of a language trick. It says, 'one' is not a dime, and did not say neither is a dime. So the answer is correct because, quarter is not a dime.



An apple is 40 cents, a banana is 60 cents , grapefruit is 80 cents. How much is a pear?


40 cents... 20 cents for each vowel in the name of the fruit
u是元音



# encoding=utf-8

you can go to a fast food restaurant to buy chicken nuggets in 6-pack, 9-pack or 20-packs. is there such a number N, such that for all numbers bigger than or equal to N, you can buy that number of chicken nuggets?




The bad numbers (number T you can't find integer solution for 6x+9y+20z=T) after 20:

21, 22, 23, 25, 28,
31, 34, 35, 37,
41, 43.

And after that, every number is good. So N=44.

(Note: only need to check 6 consecutive numbers.)




2
of 2 vote

we have to fill all these slot: 6n+1, 6n+2, 6n+3, 6n+4, 6n+5.
6n+1 gets filled by 20+20+9=49
6n+2 by 20
6n+3 by 9
6n+4 by 20+20
6n+5 by 20+9.

so start looking backwards from 49.

47 = 20+9+6+6+6
46 = 20+20+6
45 = 9+6+6+6+6+6+6
44 = 20+6+6+6+6

so, 44 is the answer...


a man has two cubes on his desk. every day he arranges both cubes so that the front faces show the current day of the month. what numbers are on the faces of the cubes to allow this?




Guys, this is the perfect solution

First cube: 0,1,2,3,4,5
Second cube: 0,1,2,6,7,8

All the combinations are possible.
But wait? where is 9 , as someone told above, 6=9=6....enjoy





A bear have to climb a 60.5 feet long hill. It climbs 3 feet in every minute before it fall down for 2 feet. How long it will take to climb the hill?


Effective feet is 1 foot overall. So till 58 feet it needs 58 minutes and then it climbs the 3 feet so it is 59 minutes overall.

The effective speed of beer is 1 foot/min , so it will take 58 minutes to climb 58 feet , then assuming his climbing speed to be uniform it will take 0.8 min to climb the next 2.5 feet. So , total time is 58.8 minutes or 59 minutes if you round it.



If one and a half teenagers, eat one and a half pizzas in one and a half days, how many pizzas can 9 teenagers eat in 3 days






A man goes to a hardware shop and asks for price of an item. The shop keeper replies that the item is "one for $1".
The man gives the shop keeper "$3 for 600". What did the man buy for his newly painted house?

Three numbers "6","0" and "0"






The buildings of an office are numbered sequentially. Person A is in building 1 and person B is in building 106. If A crosses 5 offices in a minute and B crosses 10 offices in a minute, at which office number will they both meet?
- pkala on April 25, 2014 in United States Report


At 36th building @ 8th minute.

Time     A @           B @
1          1          106
2          6          96
3          11        86
4          16        76
5          21        66
6          26        56
7          31        46
8          36        36


Find the next number in the series.

-3, 6, -18, 72, - 360



-3 x -2 = 6
6 x -3 = -18
-18 x -4 = 72
72 x -5 = -360
-360 x -6 = 2160

so next number in the series is 2160.



Find the missing number in the series.
3, 8 , 18 , _ , 78

( 3 x 2 ) + 2 = 8
( 8 x 2 ) + 2 = 18
( 18 x 2 ) + 2 = 38
( 38 x 2 ) + 2 = 78

so missing number is 38.




3, 5, 7, 9, 11, 13. Which is least like others?

9 because all other are prime numbers.






Which is a true statement?
if both true, A&B=True
A&B=False if only one false
A^B=True if only one True

第一个对的。 第二， 3个错的。 if , only限制比较大。









‘ means not. It converts a character to null in a string but converts the character to 0 in an operation
‘5 means null whereas ‘5+1=1
Which one of these is true?
Cannot recall the options; they all appeared false.
I put the last option, but couldn’t figure it out.
‘(‘5)=0?


Iam just guessing:

` converts char to null in a string and 0 in an operation.
treating ‘(‘5)=0 as an operation,
`5 becomes 0
`0 becomes 0,( no matter ` applied on what, it just converts to 0, )
0 = 0 is true..



Part of coding test for non-programmers.
Holy Water is concatenated by “Holy “.”Water” or “Holy”.” Water” Watch the space.
How would you spell "Holy water" given “Holy”=God and HOH=”Water”.
1) God.HOH
2) God.” “.HOH
3) God”.” HOH
4) Forgot others
'''