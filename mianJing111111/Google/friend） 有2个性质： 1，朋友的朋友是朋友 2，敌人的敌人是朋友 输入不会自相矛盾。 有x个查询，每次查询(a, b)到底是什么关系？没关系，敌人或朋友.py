# encoding=utf-8
'''
输入：
有n个人，m条关系（a, b, enemy/friend）
有2个性质：
1，朋友的朋友是朋友
2，敌人的敌人是朋友
输入不会自相矛盾。
有x个查询，每次查询(a, b)到底是什么关系？没关系，敌人或朋友

我是用类似floyd的思路去解的。f[a][b] = -1没关系, 0朋友, 1敌人
最终时间复杂度是O(n^3)的。


'''
