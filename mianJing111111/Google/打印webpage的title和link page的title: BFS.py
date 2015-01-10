# encoding=utf-8
#打印webpage的title和link page的title: BFS
'''
(1) 打印webpage的title和link page的title: BFS
(2) 第一题只能打印title，怎样设计unified API，使得用户可以做其他功能？java里面怎么实现的？
'''


'''
 while pre:
    cur = set([])
    for i in pre:
        # do something    可以在这里print.  调用某个函数， 做其他事情。
        search i. content and get urls
        for j in urls:
            cur.add(j)
'''


#  给多台机器，怎么bfs
#  每个node有个machine id。