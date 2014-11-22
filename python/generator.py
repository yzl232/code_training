# encoding=utf-8
a= [x*x for x in range(6)]
print a
print (x*x for x in range(6))
#这个就是generator


def city_generator():
    yield("Konstanz")
    yield("Zurich")
    yield("Schaffhausen")
    yield("Stuttgart")

x = city_generator()
print x.next()
print x.next()
print x.next()


def fibonacci1(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci1(5)
for x in f:
    print x,
print



def fibonacci2():
    """Fibonacci numbers generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci2()

counter = 0
for x in f:
    print x,
    counter += 1
    if (counter > 10): break
print


def permutations(items):
    n = len(items)
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc

for p in permutations(['r','e','d']): print ''.join(p)
for p in permutations(list("game")): print ''.join(p)


'''
A Generator of Generators
'''


def fibonacci():
    """Ein Fibonacci-Zahlen-Generator"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def firstn(g, n):
	for i in range(n):
		yield g.next()  #这个是最简单的iterator

print list(firstn(fibonacci(), 10))


