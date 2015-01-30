# encoding=utf-8
'''
d1 = a1*x1 + b1*x2 + c1*x3
d2 = a2*x1 + b2*x2 + c2*x3
d3 = a3*x1 + b3*x2 + c3*x3

Knowing all of a,b,c,d, find x1, x2, x3. As you might notice, this is high school math. But it's hard to write the code for solving it.

/*
/a1 b1 c1| /x1| /d1|
|a2 b2 c2|*|x2|=|d2|
|a3 b3 c3/ |x3/ |d3|
*/
double A[3][3], X[3], D[3];
X[0] = ?
X[1] = ?
X[2] = ?
'''


#Gaussian elimination, which reduces the matrix to a triangular one
#转换成上三角的矩阵。 然后依次代入。即可
#https://www.youtube.com/watch?v=2j5Ic2V7wq4


# encoding=utf-8
def myGauss(m):
    for i in range(len(m[0])): #基准在对角线，也就是m[i][i]， 并以m[i]
        for r in range(i+1, len(m)):   #r比i大。 也就是左下角。 而且是一列一列解决。
            t = [(1.0*rowValue * (-(m[r][i] / m[i][i]))) for rowValue in m[i]]
            m[r] = [t[j]+m[r][j]  for j in range(len(t))]
    m.reverse() #makes it easier to backsolve
    ret = [1.0*m[0][-1] / m[0][-2]]   #-1是最后一列。 直接除就可以
    for i in range(1, len(m)):
            val =m[i][-1]- sum(ret[j]*m[i][-2-j]  for j in range(i))  ##substitute in all known coefficients 代入
            ret.append(val/m[i][-2-i])   # 上一行一样的。 上一行j=i-1
    return ret[::-1]

#懂了以后就没有那么难了。

           #从-2开始。 最后一列是右边的。
            #the equation is now reduced to ax + b = c form
            #solve with (c - b) / a


print myGauss([[-3.0,2.0,-6.0,6.0],
               [5.0,7.0,-5.0,6.0],
               [1.0,4.0,-2.0,8.0]])
