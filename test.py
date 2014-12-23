a=[['a','b','c','d','e'],
    ['f','g','h','i','j'],
    ['k','l','m','n','o'],
    ['p','q','r','s','t'],
    ['u','v','w','x','y'],
    ['z','~','~','~','~']]


def trace_word(s):
    i=j=0
    x = a[i][j]
    print 'at'+x
    for x in s:
        cur = a[i][j]
        while cur != x:
            l = a[i][0];  h=a[i][len(a[i])-1]
            if l<=x<=h:
                if cur<x:
                    j+=1
                    print("Right//now we're at " + a[i][j])
                else:
                    j-=1
                    print("Left//now we're at " + a[i][j])
                cur = a[i][j]
                continue