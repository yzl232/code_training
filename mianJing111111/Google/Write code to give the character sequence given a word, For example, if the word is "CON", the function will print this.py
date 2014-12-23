# encoding=utf-8
'''
Given a set top box:
a, b, c, d, e,
f, g, h, i, j,
k, l, m, n, o
p, q, r, s, t
u, v, w, x, y
z

Write code to give the character sequence given a word, For example, if the word is "CON", the function will print this:
Right//now we're at B
Right//now we're at C
OK//to select C
Down
DOwn
Right
Right
OK//to select O
Left//now at N
OK//to select N

note: Be careful when you're at Z. if you go to the right, you will get stuck.
Afterwards, the interviewer adds a space to the right of 'Z' to test the code.
'''

a=[['a','b','c','d','e'],
    ['f','g','h','i','j'],
    ['k','l','m','n','o'],
    ['p','q','r','s','t'],
    ['u','v','w','x','y'],
    ['z','~','~','~','~']]

#因为字母都是按照顺序排列的。 所以可以判断是不是在本行。
#  low <= c <= high。  这时候向左或者右边
#三种情况。  c<low,  c>high,    low <= c <= high
def trace_word(s):
    i=j=0
    x = a[i][j]
    print('At ' + x)
    for x in s:   #  if x<'a' or x>'z'  raise exception
        cur = a[i][j]  #对于每个x用while循环来找。
        while cur!=x:
            # find min and max character in the row y
            l = a[i][0];  h = a[i][len(a[i])-1]   # in row y?
            if l <= x <= h:  #这是左右边的情况
                if cur < x: # move right
                    j+=1
                    print("Right//now we're at " + a[i][j])
                else: # move left
                    j-=1
                    print("Left//now we're at " + a[i][j])
            elif x<l: # in upper row
                i-=1
                print("Up//now we're at " + a[i][j])
            else: # in lower row
                i+=1
                print("Down//now we're at " + a[i][j])
            cur = a[i][j]
        print('OK//to select ' + x)  # while循环停止。 找到了。  每个for循环，都要找到的‘select’

if __name__ == '__main__':
    #trace_word('con')
    print '#####'
    print
    trace_word('cozmo')