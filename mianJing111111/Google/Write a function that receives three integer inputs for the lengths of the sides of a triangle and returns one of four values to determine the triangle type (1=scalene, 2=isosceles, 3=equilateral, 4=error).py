# encoding=utf-8
'''
Write a function that receives three integer inputs for the lengths of the sides of a triangle and returns one of four values to determine the triangle type (1=scalene, 2=isosceles, 3=equilateral, 4=error)
'''


'''
if(a<=0 || b<=0 || c<=0 || a+b<=c || a+c<=b || b+c<=a)
	return 4;
else if(a==b && b==c)
	return 3;
else if(a==b || b==c || a==c)
	return 2;
else
	return 1;
'''