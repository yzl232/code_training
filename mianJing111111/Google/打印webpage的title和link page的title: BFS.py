# encoding=utf-8
#打印webpage的title和link page的title: BFS
'''
(1) 打印webpage的title和link page的title: BFS
(2) 第一题只能打印title，怎样设计unified API，使得用户可以做其他功能？java里面怎么实现的？
'''


'''
visited = set(
 while pre:
    cur = set([])
    for i in pre:
        # do something    可以在这里print.  调用某个函数， 做其他事情。
        for url in i.content.urls:
            if url not in visited:
                cur.add(url)
                visied.add(url)
    pre = cur
'''


#  给多台机器，怎么bfs
#  每个node有个machine id。