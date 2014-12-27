# encoding=utf-8
def myGauss(m):
    for i in range(len(m[0])): #基准在对角线，也就是m[col][col]， 并以m[col]
        for row in range(i+1, len(m)):   #row比col大。 也就是左下角。 而且是一列一列解决。
            t = [(1.0*rowValue * (-(m[row][i] / m[i][i]))) for rowValue in m[i]]
            m[row] = [t[j]+m[row][j]  for j in range(len(t))]
    ret = [1.0*m[-1][-1]/m[-1][-2]]
    m.reverse()
    for i in range(1, len(m)):
        val = sum(   m[i][-2-j]*ret[j]   for j in range(i))
        ret.append((m[i][-1]-val)/m[i][-i-2])