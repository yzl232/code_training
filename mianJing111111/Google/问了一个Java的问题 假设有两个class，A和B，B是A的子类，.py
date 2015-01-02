# encoding=utf-8
'''
问了一个Java的问题
假设有两个class，A和B，B是A的子类，
先有下面几句
A a = new A();  #
B b = new B();
List<A> la = new List<A>();
List<B> lb = new List<B>();
（反正就是建了A，B的各一个instance，list of A 和 list of B 各一个instance）
然后问下面四句哪句能过compiler，哪句不能：
a = b;
b = a;
la = lb;
lb = la;

答案是只有第一句能过，我一开始答1和3能过（我真心不熟Java，python里面的话啥能
过啊亲）。
'''

#假设A是animal 、  B是dog