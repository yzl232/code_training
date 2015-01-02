used = [0 for _ in xrange(10)]

def check(s):
    global used
    for k in xrange(10):
        if used[k] > 1:
            return False
    return True

def min_unused():
    for i in xrange(10):
        if not used[i]:
            return i
    return -1

def add1(l):
    global used
    n = len(l)
    k = c = t = pos = -1
    for i in xrange(n-1, -1, -1):
        c = l[i]
        t = (c+1) % 10
        if not used[t]:
            pos = i
            k = c
            break
    if k == -1:
        return False       
    if k == 9:
        l[pos] = 0
        used[0] = 1
        used[9] = 0       
        m = min_unused()       
        if m == -1:
            return None
        used[m] = 1
        if pos == 0:
            l.insert(0, m)
        else:
            used[l[pos-1]] = 0
            l[pos-1] = m
    else:
        x = l[pos]
        used[x] = 0
        l[pos] = x+1
        used[x+1] = 1
    return True           

def swap(l):
    n = len(l)
    for i in xrange(n-1, -1, -1):
        for j in xrange(i-1, -1, -1):
            if l[j] < l[i]:
                l[i],l[j] = l[j],l[i]
                return True
    return False   

def tolist(num):
    r = []
    while num:
        r.append(num % 10)
        num /= 10
    return r[::-1]

def tonum(l):
    r = 0
    for x in l:
        r *= 10
        r += x
    return r

# @input num is an integer   
def get_next_bigger(num):
    global used
    for i in xrange(10):
        used[i] = 0
    l = tolist(num)
    for i in l:
        used[i] += 1
        if used[i] > 1:
            return None
    if add1(l):
        return tonum(l)
    if swap(l):
        return tonum(l)
    return None

def test3():
    #num = 1234567980
    num = 1
    cnt = 0
    while num:
        print num
        cnt += 1
        if cnt == 50:
            break
        num = get_next_bigger(num)
    #while

if __name__ == "__main__":
    test3()
